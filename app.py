import streamlit as st
import hashlib
import bcrypt
import time
import itertools
import string
import pandas as pd

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Password Cracking Lab",
    page_icon="🔐",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>
.main {
    background-color: #0b1020;
    color: white;
}

.stApp {
    background-color: #0b1020;
    color: white;
}

h1, h2, h3, h4 {
    color: white !important;
}

.stTextInput input {
    background-color: #151c2e;
    color: white;
}

.stButton button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 0.5rem 1rem;
}

.metric-box {
    background-color: #151c2e;
    padding: 1rem;
    border-radius: 12px;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.title("Password Cracking Lab")
st.markdown(
    "Four interactive labs • Hashing • Wordlist attacks • Brute force • Defense"
)

tabs = st.tabs([
    "🔢 Lab 1 · Hashing",
    "📋 Lab 2 · Wordlist Attack",
    "⌨️ Lab 3 · Brute Force",
    "🛡️ Lab 4 · Defense"
])

# =========================================================
# LAB 1 — HASHING
# =========================================================

with tabs[0]:

    st.header("What is Hashing?")

    st.info(
        "A hash function converts a password into a fixed-length string. "
        "Websites store hashes instead of actual passwords."
    )

    password = st.text_input(
        "Type any password:",
        placeholder="e.g. hello123"
    )

    if password:

        md5_hash = hashlib.md5(password.encode()).hexdigest()
        sha1_hash = hashlib.sha1(password.encode()).hexdigest()
        sha256_hash = hashlib.sha256(password.encode()).hexdigest()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("MD5 Length", len(md5_hash))

        with col2:
            st.metric("SHA1 Length", len(sha1_hash))

        with col3:
            st.metric("SHA256 Length", len(sha256_hash))

        st.subheader("Generated Hashes")

        st.code(f"MD5:\n{md5_hash}")
        st.code(f"SHA1:\n{sha1_hash}")
        st.code(f"SHA256:\n{sha256_hash}")

        st.warning(
            "MD5 and SHA1 are considered weak for password storage today."
        )

# =========================================================
# LAB 2 — WORDLIST ATTACK
# =========================================================

with tabs[1]:

    st.header("Wordlist Attack Simulation")

    st.markdown(
        "A wordlist attack tries common passwords until a matching hash is found."
    )

    common_passwords = [
        "123456",
        "password",
        "admin",
        "welcome",
        "hello",
        "hello123",
        "qwerty",
        "letmein"
    ]

    target_password = st.selectbox(
        "Choose target password:",
        common_passwords
    )

    target_hash = hashlib.md5(target_password.encode()).hexdigest()

    st.code(f"Target MD5 Hash:\n{target_hash}")

    if st.button("Start Wordlist Attack"):

        progress = st.progress(0)

        found = False

        for i, pwd in enumerate(common_passwords):

            time.sleep(0.4)

            hashed = hashlib.md5(pwd.encode()).hexdigest()

            st.write(f"Trying: {pwd}")

            progress.progress((i + 1) / len(common_passwords))

            if hashed == target_hash:
                st.success(f"PASSWORD FOUND: {pwd}")
                found = True
                break

        if not found:
            st.error("Password not found.")
            
            st.divider()

    st.subheader("📂 Upload Hash File")

    uploaded_file = st.file_uploader(
        "Upload a .txt file containing MD5 hashes",
        type=["txt"]
    )

    if uploaded_file:

        file_content = uploaded_file.read().decode("utf-8")

        hashes = [
            line.strip()
            for line in file_content.splitlines()
            if line.strip()
        ]

        st.write(f"Loaded {len(hashes)} hash(es).")

        crack_results = []

        wordlist = [
            "123456",
            "password",
            "admin",
            "welcome",
            "hello",
            "hello123",
            "qwerty",
            "letmein"
        ]

        for target_hash in hashes:

            found_password = None

            for pwd in wordlist:

                hashed_pwd = hashlib.md5(
                    pwd.encode()
                ).hexdigest()

                if hashed_pwd == target_hash:
                    found_password = pwd
                    break

            crack_results.append({
                "Hash": target_hash,
                "Cracked Password": found_password if found_password else "Not Found"
            })

        df_results = pd.DataFrame(crack_results)

        st.subheader("🔓 Crack Results")

        st.dataframe(df_results)

# =========================================================
# LAB 3 — BRUTE FORCE
# =========================================================

with tabs[2]:

    st.header("Brute Force Simulation")

    st.markdown(
        "Brute force tries every possible combination until the password is cracked."
    )

    brute_password = st.text_input(
        "Choose a short password (max 3 lowercase letters)",
        value="abc"
    )

    if len(brute_password) > 3:
        st.warning("Use maximum 3 characters for demo.")
    else:

        target_hash = hashlib.md5(brute_password.encode()).hexdigest()

        st.code(f"Target Hash:\n{target_hash}")

        if st.button("Start Brute Force"):

            chars = string.ascii_lowercase

            found = False

            attempts = 0

            output = st.empty()

            for length in range(1, 4):

                for combo in itertools.product(chars, repeat=length):

                    guess = ''.join(combo)

                    attempts += 1

                    output.write(f"Trying: {guess}")

                    hashed_guess = hashlib.md5(
                        guess.encode()
                    ).hexdigest()

                    if hashed_guess == target_hash:

                        st.success(f"Password cracked: {guess}")
                        st.info(f"Attempts: {attempts}")

                        found = True
                        break

                if found:
                    break

# =========================================================
# LAB 4 — DEFENSE
# =========================================================

with tabs[3]:

    st.header("Password Defense")

    st.markdown(
        "Strong password storage uses bcrypt instead of MD5 or SHA1."
    )

    secure_password = st.text_input(
        "Enter password for bcrypt hashing:",
        type="password"
    )

    if secure_password:

        hashed = bcrypt.hashpw(
            secure_password.encode(),
            bcrypt.gensalt()
        )

        st.subheader("bcrypt Hash")

        st.code(hashed.decode())

        st.success(
            "bcrypt adds salting and is much harder to crack."
        )

    st.divider()

    st.subheader("Best Practices")

    st.markdown("""
✅ Use long passwords  
✅ Use uppercase + lowercase + symbols  
✅ Enable MFA  
✅ Use bcrypt or Argon2  
✅ Never store plain-text passwords  
✅ Rate limit login attempts  
""")

    # ---------------- KEYSPACE TABLE ---------------- #

    st.subheader("📈 Keyspace Explosion")

    st.markdown(
        """
        Every additional character massively increases the number of possible passwords.
        This is why long passwords are dramatically harder to brute force.
        """
    )

    charsets_ks = [
        ("Digits only (0-9)", 10),
        ("Lowercase letters", 26),
        ("Letters + digits", 36),
        ("Upper + lower + digits", 62),
        ("All keyboard chars", 95),
    ]

    lengths_ks = [4, 6, 8, 10, 12]

    def fmt_num(n):
        return f"{n:,}"

    ks_table = {
        "Character set": [r[0] for r in charsets_ks]
    }

    for ln in lengths_ks:
        ks_table[f"{ln} chars"] = [
            fmt_num(r[1] ** ln)
            for r in charsets_ks
        ]

    df = pd.DataFrame(ks_table)

    st.table(df)

    st.warning(
        "Going from 8 → 12 lowercase characters multiplies the "
        "keyspace massively, making brute force attacks impractical."
    )
    
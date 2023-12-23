function isAuthCheck() {
    try {
        if (
            JSON.parse(localStorage.userInfo).Success === "Login successfully"
        ) {
            return JSON.parse(localStorage.userInfo).email;
        }
    } catch (e) {
        return false;
    }
    return true
}

export default isAuthCheck;
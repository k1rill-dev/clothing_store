import {useState} from "react";
import {Navigate, redirect} from "react-router-dom";
import Form from '../../utilities/Forms'
import axios from 'axios'
import React from 'react'
import ReactDOM from 'react-dom'


function getCookie(name) {
        if (!document.cookie) {
            return null;
        }

        const xsrfCookies = document.cookie.split(';')
            .map(c => c.trim())
            .filter(c => c.startsWith(name + '='));

        if (xsrfCookies.length === 0) {
            return null;
        }
        return decodeURIComponent(xsrfCookies[0].split('=')[1]);
    }
async function loginUser(dataUser) {
    try {
        const {data, status} = await axios.post(
            'http://localhost:8000/api/v1/token/login',
            dataUser,
            {
                headers: {
                    'Content-Type': 'application/json',
                    Accept: 'application/json',

                },
                withCredentials: true
            }
        );
        console.log(data)
        return data;
    } catch (error) {
        if (axios.isAxiosError(error)) {
            console.log('error message: ', error.message);
            return error.message;
        } else {
            console.log('unexpected error: ', error);
            return 'An unexpected error occurred';
        }
    }
}


const Login = () => {

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [validate, setValidate] = useState({});
    const [showPassword, setShowPassword] = useState(false);


    const validateLogin = () => {
        let isValid = true;

        let validator = Form.validator({
            email: {
                value: email,
                isRequired: true,
                isEmail: true
            },
            password: {
                value: password,
                isRequired: true,
                minLength: 1
            }
        });

        if (validator !== null) {
            setValidate({
                validate: validator.errors
            })

            isValid = false
        }
        return isValid;
    }

    const authenticate = async (e) => {
        e.preventDefault();

        const validate = validateLogin();

        if (validate) {
            let userData = {
                "email": email,
                "password": password
            }
            const userInfo = await loginUser(userData).then(
                r => {
                    return JSON.stringify(r, null, 4)
                })
            try {
                if ("Success" in JSON.parse(userInfo))
                    localStorage.setItem("userInfo", userInfo);
                window.location.reload();
            } catch (e) {

            }}
    }

    const togglePassword = (e) => {
        if (showPassword) {
            setShowPassword(false);
        } else {
            setShowPassword(true)
        }
    }
    try {
        if (JSON.parse(localStorage.userInfo).Success === "Login successfully")
            console.log(JSON.parse(localStorage.userInfo).Success === "Login successfully")
        return (<Navigate to={"/"}/>)
    } catch (e) {
        return (
            <div className="row g-0 auth-wrapper">
                <div className="col-12 col-md-5 col-lg-6 h-100 auth-background-col">
                    <div className="auth-background-holder"></div>
                    <div className="auth-background-mask"></div>
                </div>

                <div className="col-12 col-md-7 col-lg-6 auth-main-col text-center">
                    <div className="d-flex flex-column align-content-end">
                        <div className="auth-body mx-auto">
                            <p>Войдите в свой аккаунт</p>
                            <div className="auth-form-container text-start">
                                <form className="auth-form" method="POST" onSubmit={authenticate} autoComplete={'off'}>
                                    <div className="email mb-3">
                                        <input type="email"
                                               className={`form-control ${validate.validate && validate.validate.email ? 'is-invalid ' : ''}`}
                                               id="email"
                                               name="email"
                                               value={email}
                                               placeholder="Почта"
                                               onChange={(e) => setEmail(e.target.value)}
                                        />

                                        <div
                                            className={`invalid-feedback text-start ${(validate.validate && validate.validate.email) ? 'd-block' : 'd-none'}`}>
                                            {(validate.validate && validate.validate.email) ? validate.validate.email[0] : ''}
                                        </div>
                                    </div>

                                    <div className="password mb-3">
                                        <div className="input-group">
                                            <input type={showPassword ? 'text' : 'password'}
                                                   className={`form-control ${validate.validate && validate.validate.password ? 'is-invalid ' : ''}`}
                                                   name="password"
                                                   id="password"
                                                   value={password}
                                                   placeholder="Пароль"
                                                   onChange={(e) => setPassword(e.target.value)}
                                            />

                                            <button type="button" className="btn btn-outline-primary btn-sm"
                                                    onClick={(e) => togglePassword(e)}><i
                                                className={showPassword ? 'far fa-eye' : 'far fa-eye-slash'}></i>
                                            </button>

                                            <div
                                                className={`invalid-feedback text-start ${(validate.validate && validate.validate.password) ? 'd-block' : 'd-none'}`}>
                                                {(validate.validate && validate.validate.password) ? validate.validate.password[0] : ''}
                                            </div>
                                        </div>
                                    </div>
                                    <div className="text-center">
                                        <button type="submit" className="btn btn-primary w-100 theme-btn mx-auto"
                                                onClick={authenticate}>Войти
                                        </button>
                                    </div>
                                </form>

                                <hr/>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        );
    }

}

export default Login;
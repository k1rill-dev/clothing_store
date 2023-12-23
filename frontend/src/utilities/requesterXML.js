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

function requesterXML(method, url, isAsync, body = null) {
    let req = new XMLHttpRequest();
    req.open(method, url, isAsync);
    let token = getCookie('csrftoken')
    req.setRequestHeader('Content-Type', 'application/json')
    req.setRequestHeader('X-CSRFToken', token)
    req.withCredentials = true
    req.send(body);
    return JSON.parse(req.responseText)
}
export default requesterXML;
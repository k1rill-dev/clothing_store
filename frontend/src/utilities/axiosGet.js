import axios from "axios";

export default async function getWithAxios(url){
    try {
        const {data, status} = await axios.get(
            url,
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
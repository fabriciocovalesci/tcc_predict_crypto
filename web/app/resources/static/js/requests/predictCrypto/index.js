


const BASE_URL = "http://127.0.0.1:5000/"



async function get_corr_home() {
    try {
        const resp = await axios.get(`${BASE_URL}corr`);
            if (typeof resp.data !== undefined){
                return resp.data;
            }
    } catch (err) {
        console.error(err);
    }
};
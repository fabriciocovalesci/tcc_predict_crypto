






async function get_corr_home() {
    try {
        const resp = await axios.get(`http://127.0.0.1:5000/corr`);
        console.log('adsaoas');
            if (typeof resp.data !== undefined){
                return resp.data;
            }
    } catch (err) {
        console.error(err);
    }
};
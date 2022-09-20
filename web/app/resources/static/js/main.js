
const BASE_URL = "http://127.0.0.1:5000"


function get_day(day, crypto) {
  if (day && crypto) {
    axios({
      method: 'post',
      url: `${BASE_URL}/predict`,
      headers: {
        'Content-Type': 'application/json',
      },
      data: {
        "period": day,
        "crypto": crypto
      }
    })
      .then((response) => {
        console.log(response);
      }, (error) => {
        console.log(error);
      });
  }
}



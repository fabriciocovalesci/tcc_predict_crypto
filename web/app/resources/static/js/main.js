
const BASE_URL = "http://127.0.0.1:5000"


function format_date(date){
  let year = date.split('-')[0]
  let month = date.split('-')[1]
  let day = date.split('-')[2]
  return `${day}/${month}/${year}`
}


function construct_tr(day, price){
  tr = `
    <tr class="table-success">
        <th scope="row">${day}</th>
        <td>${price}</td>
    </tr>
  `
  return tr
}


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
          $( "#tbody-predict" ).empty();
          response.data.map((elem) => {
          let tr = construct_tr(format_date(elem.day), elem.price)
          $("#tbody-predict").append(tr);
        })
      }, (error) => {
        console.log(error);
      });
  }
}



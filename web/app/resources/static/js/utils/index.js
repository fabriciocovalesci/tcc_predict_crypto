


function format_date(date) {
    let year = date.split('-')[0]
    let month = date.split('-')[1]
    let day = date.split('-')[2]
    return `${day}/${month}/${year}`
}


function format_currency(currency) {
    const value = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(currency);
    return value
}



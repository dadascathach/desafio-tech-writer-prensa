$(document).ready(function(){
  $('#send').click(function(){
    let number = $('#input').val()

    $.ajax({
      url: "http://localhost:8070/api/" + number,
      success: function(data) {
        data = JSON.parse(data)
        let services = data['data']['bin']['services']
        let name = null
        let description = null

        if (services.length > 0) {
          JQuery.each(services, function(idx, row){
            name = row['name']
            description = row['description']

            $('.result').append("<span>Name: " + name + "</span><br><span>Description: " + description + "</span")
          })
        }
        
        $('.result').append("<span>Name: " + name + "</span><br><span>Description: " + description + "</span")
      }
    })
  })
});
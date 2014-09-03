var idea = ['red', 'black', 'blue', 'green', 'yellow'];

$('#give').click(function(){
  var index = Math.round(Math.random()*(idea.length - 1));
  $('input').val(idea[index]);
  console.log(index);
})

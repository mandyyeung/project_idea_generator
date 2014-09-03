var idea = ['red', 'black', 'blue', 'green', 'yellow'];
var previousIndex = null;

$('#give').click(function(){
  $('input').val(idea[getIndex()]);
})

function getIndex() {
	var index = Math.round(Math.random()*(idea.length - 1));
	if (index === previousIndex) {
		console.log("Previous index already used")
		index = getIndex();
	}
	previousIndex = index;
	return index;
}
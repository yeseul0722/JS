axios.get('https://api.example.com/data')
	.then(function (response) {
	console.log(response)
})
.catch(function (err){
	console.log(err)
})
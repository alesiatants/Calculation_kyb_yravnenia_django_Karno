$(".b").click(function(){
	if ($('#a').val() && $('#a').val()!=0 && $('#b').val() && $('#c').val()&& $('#d').val()){
		
		if (confirm("Вы действительно хотите отправить форму?")) {
			
				return true;
				
		} else {
				return false;
		}
	}
		else{
			alert("Не все поля заполнены правильно!");
			return false;
		}
});
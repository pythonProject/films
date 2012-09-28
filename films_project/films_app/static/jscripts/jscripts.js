function addGenre1()
{
	if($("#addGenreBlock").css("display") == "none")
	{
		$("#addGenreBlock").css("display", "block");
		$("#addGenreButton").val("Скрыть поле");
	}
	else
	{
		$("#addGenreBlock").css("display", "none");
		$("#addGenreButton").val("Добавить жанр");		
	}
}
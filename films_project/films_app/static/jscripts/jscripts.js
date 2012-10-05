$(document).ready(function()
{
	$("#id_authors").focus(function()
	{
		if($("#f").css("display") == "none")
			$("#f").css("display", "block");
	});
	$("#f").blur(function()
	{
		$("#f").css("display", "none");
	});
	$("#id_authors").keyup(function()
		{
			var str = $("#id_authors").val();
			c = $("#f li").length;
			var str2;
			var i = 0;
			for(i = 0; i < c; i++)
			{
				if($("#f li").eq(i).text().indexOf(str) === -1)
				{	
					$("#f li").eq(i).css("display", "none");
				}
				else
				{
					$("#f li").eq(i).css("display", "block");
				}
			}
		});
	$("#f li").click(function()
	{
		alert($(this).get());
	});
});
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
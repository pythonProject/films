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
$(document).ready(function()
{
	$("#id_authors").focus(function()
	{
		if($("#authors_list").css("display") == "none")
			$("#authors_list").css("display", "block");
		if($("#authors_list li").text() == "")
		{
			var c = $("#f li").length;
			var v;
			for( var i = 0; i < c; i++)
			{
				v = $("#f li").eq(i).text();
				$("#authors_list").append("<li>" + v + "</li>");
			}
		}
	});
	$("#id_authors").blur(function()
	{
		$("#authors_list").css("display", "none");
	});
	$("#id_authors").keyup(function()
		{
			var str = $("#id_authors").val();
			c = $("#authors_list li").length;
			var str2;
			var i = 0;
			for(i = 0; i < c; i++)
			{
				if($("#authors_list li").eq(i).text().indexOf(str) === -1)
				{	
					$("#authors_list li").eq(i).css("display", "none");
				}
				else
				{
					$("#authors_list li").eq(i).css("display", "block");
				}
			}
		});
});

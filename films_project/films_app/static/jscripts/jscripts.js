$(document).ready(function()
{
    var authors_list_loaded = 0;
    $("#id_add_authors").focus(function()
    {
        if($("#f").css("display") == "none")
            $("#f").css("display", "block");
    });
    $("#f").children("li").blur(function()
    {
        $("#f").css("display", "none");
        for(var i = 0; i < $("#f li").length; i++)
        {
            $("#f li").eq(i).css("display", "none");
        }
    });
    $("#id_add_authors").keyup(function(e)
        {
            $("#added_author").css("display", "none");
            if(e.which === 13)
            {
                var str = $("#id_add_authors").val().trim();
                var c = $("#f li").length;
                var am = 0;
                var amount = 0;
                for(var i = 0; i < c; i++)
                {
                    if($("#f li").eq(i).text().trim() === str & $("#f li").eq(i).css("display") !== "none")
                    {
                        $("#authors_list").append("<li style='list-style-type: none'><input type='checkbox' id='id_" + $("#f li").eq(i).text() + "' checked='checked' onChange='removeAuthor($(this))' /> <span id='id_" + $("#f li").eq(i).text() + "'>" + $("#f li").eq(i).text() + "</span></li>");
                        $("#f li").eq(i).css("display", "none");
                        am++;
                        break;
                    }
                }
                if(am == 0)
                {
                    for(var j = 0; j < $("#authors_list li").length; j++)
                    {
                        if(str == $("#authors_list li").eq(j).children("span").text().trim())
                            amount++;
                    }
                    if(amount == 0)
                    {
                        $("#authors_list").append("<li style='list-style-type: none'><input type='checkbox' id='id_" + $("#id_add_authors").val() + "' checked='checked' onChange='removeAuthor($(this))' /> <span id='id_" + $("#id_add_authors").val() + "'>" + $("#id_add_authors").val() + "</span></li>");
                    }
                    else
                    {
                        $("#added_author").css("display", "block");
                    }
                }
            }
            else
            {
                var str = $("#id_add_authors").val();
                var c = $("#f li").length;
                for(var i = 0; i < c; i++)
                {
                    if($("#f li").eq(i).text().indexOf(str) === -1)
                    {
                        $("#f li").eq(i).css("display", "none");
                    }
                    else
                    {
                        if($("#authors_list li").length == 0)
                        {
                            for(var g = 0; g < $("#f li").length; g++)
                                $("#f li").eq(i).css("display", "block");
                        }
                        for(var j = 0; j < $("#authors_list li").length; j++)
                        {
                            if($("#authors_list li").eq(j).children("span").text() === $("#f li").eq(i).text())
                            {
                                $("#f li").eq(i).css("display", "none");
                                break;
                            }
                            else
                            {
                                $("#f li").eq(i).css("display", "block");
                            }
                        }
                    }
                }
            }
        });
    $("#f li").click(function()
    {
        $("#authors_list").append("<li style='list-style-type: none'><input type='checkbox' id='id_" + $(this).text() + "' checked='checked' onChange='removeAuthor($(this))' /> <span id='id_" + $(this).text() + "'>" + $(this).text() + "</span></li>");
        $(this).css("display", "none");
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

function removeAuthor(obj)
{
    var am = 0;
    for(var i = 0; i < $("#f li").length; i++)
    {
        if($("#f li").eq(i).text().trim() == obj.next().text().trim())
        {
            $("#f li").eq(i).css("display", "block");
            obj.parent().detach();
            am++;
        }
    }
    if(am == 0)
    {
        obj.parent().detach();
    }
}
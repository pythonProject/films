$(document).ready(function()
{
    $("#id_add_authors").focus(function()
    {
        $("#hide_authors").css("display", "block");
        if($("#f").css("display") == "none")
            $("#f").css("display", "block");
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
        $("#authors_list").append("<li><input type='checkbox' id='id_" + $(this).text() + "' checked='checked' onChange='removeAuthor($(this))' /> <span id='id_" + $(this).text() + "'>" + $(this).text() + "</span></li>");
        $(this).css("display", "none");
    });
    $("#id_actors").focus(function()
    {
        $("#actors_exists").css("display", "block");
        $("#hideActors").css("display", "block");
    });
    $("#actors_exists li").click(function()
    {
        var c = $("#actors_list li").length;
        var err = 0;
        for(var i = 0; i < c; i++)
        {
            if($(this).text().trim() == $("#actors_list li").eq(i).text().trim())
            {
                $("#actor_added").css("display", "block");
                err++;
            }
        }
        if(!err)
        {
            $("#actors_list").append("<li style='list-style-type:none;'><input type='checkbox' onChange='removeActor($(this))' checked='checked' id='" + $(this).text().trim() + "'/>" + $(this).text().trim() + "</li>");
            $(this).css("display", "none");
        }
    });
    $("#id_actors").keyup(function(e)
    {
        $("#actor_added").css("display", "none");
        if(e.which == 13)
        {
            var err = 0;
            for(var i = 0; i < $("#actors_list li").length; i++)
            {
                if($("#id_actors").val().trim() == $("#actors_list li").eq(i).text().trim())
                {
                    $("#actor_added").css("display", "block");
                    err++;
                }
            }
            for(var i = 0; i < $("#actors_exists li").length; i++)
            {
                if($("#id_actors").val().trim() == $("#actors_exists li").eq(i).text().trim())
                {
                    $("#actors_exists li").eq(i).css("display", "none");
                }
            }
            if(!err)
            {
                $("#actors_list").append("<li style='list-style-type:none;'><input type='checkbox' onChange='removeActor($(this))' checked='checked' id='" + $("#id_actors").val().trim() + "'/>" + $("#id_actors").val().trim() + "</li>");
                $("#id_actors").val("");
                for(var i = 0; i < $("#actors_exists li").length; i++)
                {
                    var flag = 0;
                    for(var j = 0; j < $("#actors_list li").length; j++)
                    {
                        if($("#actors_exists li").eq(i).text().trim() == $("#actors_list li").eq(j).text().trim())
                        flag++;
                    }
                    if(!flag)
                        $("#actors_exists li").eq(i).css("display", "block");
                }
            }
        }
        else
        {
            var str = $("#id_actors").val().trim();
            for(var i = 0; i < $("#actors_exists li").length; i++)
            {
                if($("#actors_exists li").eq(i).text().trim().indexOf(str) == -1)
                {
                    $("#actors_exists li").eq(i).css("display", "none");
                }
                else
                {
                    $("#actors_exists li").eq(i).css("display", "block");
                }
            }
        }
    });
    $("#id_addGenre").keyup(function(e)
    {
        $("#form_is_empty").css("display", "none");
        $("#added_genre").css("display", "none");
        var c = 0;
//        alert($("#id_addGenre").val());
        if(e.which == 13)
        {
            if($("#id_addGenre").val() == "")
            {
                $("#form_is_empty").css("display", "block");
                c++;
            }
            for(var i = 0; i < $("#list_genres li").length; i++)
            {
//                alert($("#list_genres li").eq(i).text());
                if($("#id_addGenre").val().trim() == $("#list_genres li").eq(i).text())
                {
                    $("#added_genre").css("display", "block");
                    c++;
                }
            }
            if(c == 0)
            {
                $("#list_genres").append("<li style='list-style-type: none;'><input type='checkbox' checked='checked' id='" + $("#id_addGenre").val() + "' />" + $("#id_addGenre").val() + "</li>");
                $("#id_addGenre").val("");
            }
        }
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

function HideAuthors(obj)
{
    $("#f").css("display", "none");
    obj.css("display", "none");
}

function HideActors()
{
    $("#actors_exists").css("display", "none");
    $("#hideActors").css("display", "none");
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
function removeActor(obj)
{
    for(var i = 0; i < $("#actors_exists li").length; i++)
    {
        if(obj.parent().text().trim() == $("#actors_exists li").eq(i).text().trim())
        {
            $("#actors_exists li").eq(i).css("display", "block");
        }
    }
    obj.parent().detach();
}
$(document).ready(function()
{
    $("#shortSearchSubmit").click(function(){
        $("#shortSearchForm").submit();
    });
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
                        $("#authors_list").append("<span><input type='checkbox' name='author_" + $("#f li").eq(i).text() + "' id='id_" + $("#f li").eq(i).text() + "' checked='checked' onChange='removeAuthor($(this))' /> <span id='id_" + $("#f li").eq(i).text() + "'>" + $("#f li").eq(i).text() + "</span></span>");
                        $("#f li").eq(i).css("display", "none");
                        $("#id_add_authors").val("");
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
                        $("#authors_list").append("<span><input type='checkbox' name='author_" + $("#id_add_authors").val() + "' id='id_" + $("#id_add_authors").val() + "' checked='checked' onChange='removeAuthor($(this))' /> <span id='id_" + $("#id_add_authors").val() + "'>" + $("#id_add_authors").val() + "</span></span>");
                        $("#id_add_authors").val("");
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
        $("#authors_list").append("<span><input type='checkbox' id='id_" + $(this).text() + "' checked='checked' name='author_" + $(this).text() + "' onChange='removeAuthor($(this))' /> <span id='id_" + $(this).text() + "'>" + $(this).text() + "</span></span>");
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
            $("#actors_list").append("<span style='list-style-type:none;'><input type='checkbox' onChange='removeActor($(this))' checked='checked' name='actor_" + $(this).text().trim() + "' id='" + $(this).text().trim() + "'/>" + $(this).text().trim() + "</span>");
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
                $("#actors_list").append("<span style='list-style-type:none;'><input type='checkbox' onChange='removeActor($(this))' checked='checked' name='actor_" + $("#id_actors").val().trim() + "' id='" + $("#id_actors").val().trim() + "'/>" + $("#id_actors").val().trim() + "</span>");
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
        if(e.which == 13)
        {
            if($("#id_addGenre").val() == "")
            {
                $("#form_is_empty").css("display", "block");
                c++;
            }
            for(var i = 0; i < $("#list_genres li").length; i++)
            {
                if($("#id_addGenre").val().trim() == $("#list_genres li").eq(i).text())
                {
                    $("#added_genre").css("display", "block");
                    c++;
                }
            }
            if(c == 0)
            {
                $("#list_genres").append("<li style='list-style-type: none;'><input type='checkbox' checked='checked' name='genre_" + $("#id_addGenre").val() + "' id='" + $("#id_addGenre").val() + "' />" + $("#id_addGenre").val() + "</li>");
                $("#id_addGenre").val("");
            }
        }
    });
    $("#login").click(function()
    {
        $("#login_div").toggle(1000);
        //$("#login").attr("class", "img_logout") ? $("#login").attr("class") == "img_login" : $("#login").attr("class", "img_login");
        if($("#login").attr("class") == "img_login")
        {
            $("#login").attr("class", "img_logout");
        }
        else
        {
            $("#login").attr("class", "img_login");
        }
    });
    $("#ExtSearch").click(function()
    {
        $("#searchFormExt").toggle(1000);
    });
    $("#submit_id").live('click', function()
    {
        $("#uploadFilmForm").submit();
    });
    $("#submit_search").live('click', function()
    {
        $("#searchForm").submit();
    });
    $("#searchFormSubmit").click(function()
    {
        window.searchForm.submit();
    });
    SendMessage();
    var intervalId = window.setInterval(function(){
        $.ajax({
            url: "/chat/",
            type: "GET",
            dataType: "json",
            data: "",
            success: function(data){
                $("#chatBox").val("");
                for(var i = 0; i < data.length; i++){
                    var text = $("#chatBox").val();
                    $("#chatBox").val(text + data[i].user +
                        "(" + data[i].time + "): " +
                        data[i].message + "\n");
                }
            }
        });
        $.ajax({
            url: "/comment/",
            type: "GET",
            dataType: "json",
            data: "film=" + window.location.href.split("=")[1],
            success: function(data){
                var existentId = $("#CommentList li")[$("#CommentList li").length - 1].children[0].textContent;
                var newId = data[data.length - 1].id.toString();
                if(existentId !== newId){
                    $("#CommentList").append("<li>" + data[data.length - 1].user +
                        " (" + data[data.length - 1].time + "): " +
                        data[data.length - 1].message +
                        "<span style='display: none'>" + data[data.length - 1].id +
                        "</span></li>");
                }
            }
        });
    }, 1000);
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
function checkLogin()
{
    if($("#id_login").val() == "" || $("#id_password").val() == "")
    {
        $("#emptyField").css("display", "block");
        $("#login_error").css("display","none");
        return;
    }
    else
    {
        $("#emptyField").css("display", "none");
    }
    $.ajax(
        {
            url: '/login_ajax/',
            type: "POST",
            dataType: "json",
            data: "login=" + $("#id_login").val().trim() + "&password=" + $("#id_password").val().trim() + "&csrfmiddlewaretoken=" + $("[name=csrfmiddlewaretoken]").val().trim() + "&is_ajax=True",
            success: function (data)
            {
                if(data.error)
                {
                    $("#login_error").css("display","block");
                }
                else
                {
                    window.location.href = "/logged_in/";
                }
            }
        });
}
$('#id_releaseDate').DatePicker({
    format:'Y-m-d',
    date: $('#id_releaseDate').val(),
    current: $('#id_releaseDate').val(),
    starts: 1,
    position: 'r',
    onBeforeShow: function(){
        $('#id_releaseDatee').DatePickerSetDate($('#id_releaseDate').val(), true);
    },
    onChange: function(formated, dates){
        $('#id_releaseDate').val(formated);
        if ($('#closeOnSelect input').attr('checked')) {
            $('#id_releaseDate').DatePickerHide();
        }
    }
});
function ChangePage(page)
{
    var arr = document.location.href.split("&");
    if(arr[0].indexOf("page=") != -1)
    {
        arr[0] = arr[0].split("=")[0] + "=" + page.toString();
    }
    else
    {
        var arr1 = arr[0].split("?");
        arr1[0] = arr1[0] + "?page=" + page.toString();
        if(arr.length > 1)
            arr[0] = arr1[0] + "&" + arr1[1];
        else
            arr[0] = arr1[0];
    }
    var url = arr.join("&");
    document.location.href = url;
}

function Like(film, action){
    var act = action == "+" ? "like": "dislike";
    $.ajax({
            url: '/like/',
            type: "GET",
            dataType: "json",
            data: "name=" + film + "&action=" + act,
            success: function (data)
            {
                if(!data.error)
                {
                    if(act == "like")
                    {
                        var likes = parseInt($("#like").text()) + 1;
                        $("#like").text(likes);
                    }
                    else
                    {
                        var dislikes = parseInt($("#dislike").text()) + 1;
                        $("#dislike").text(dislikes);
                    }
                }
            }
        });
}
function SendMessage(){
    $.ajax({
        url: "/chat/",
        type: "GET",
        dataType: "json",
        data: "message=" + $("#chatMessage").val().trim(),
        success: function(data){
            if($("#chatMessage").val() !== ""){
                $("#chatMessage").val("");
                $("#chatBox").val("");
                for(var i = 0; i < data.length; i++){
                    var text = $("#chatBox").val();
                    $("#chatBox").val(text + data[i].user +
                                      "(" + data[i].time + "): " +
                                      data[i].message + "\n");
                }
            }
            else{
                for(var i = 0; i < data.length; i++){
                    var text = $("#chatBox").val();
                    $("#chatBox").val(text + data[i].user +
                        "(" + data[i].time + "): " +
                        data[i].message + "\n");
                }
            }
        }
    });
}

function SendComment(){
    $.ajax({
        url: "/comment/",
        type: "GET",
        dataType: "json",
        data: "comment=" + $("#Comment").val() + "&film=" + window.location.href.split("=")[1],
        success: function(data){
            $("#Comment").val("");
            var len = data.length - 1;
            $("#CommentList").append("<li>" + data[len].user +
                                     " (" + data[len].time + "): " +
                                     data[len].message +
                                     "<span style='display: none'>" + data[data.length - 1].id +
                                     "</span></li>");
        }
    });
}

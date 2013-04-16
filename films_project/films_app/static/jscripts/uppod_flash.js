//	JS API 2.0 для Uppod 1+ http://uppod.ru/player/js

// события - http://uppod.ru/player/js#events

function uppodEvent(playerID,event) {

    switch(event){

        case 'init': // загрузка

            break;

        case 'start': // старт
            film_name = window.location.href.split("=")[1].split("%20").join(" ");
            $.ajax({
                url: "/like/",
                type: "GET",
                dataType: "json",
                data: "name=" + film_name + "&action=start",
                success: function(data){
                    if(!data["error"])
                    {
                        var ex = parseInt($("#examinations").text()) + 1;
                        $("#examinations").text(ex);
                    }
                }
            });
            break;
        case 'play': // пуск
            break;

        case 'pause': // пауза

            break;

        case 'stop': // стоп

            break;

        case 'seek': // перемотка

            break;

        case 'loaded': // перемотка

            break;

        case 'end': // конец воспроизведения

            break;

        case 'download': // скачивание

            break;

        case 'quality': // переключение качества

            break;

        case 'error': // ошибка (файл не найден)

            break;

        case 'ad_end': // окончание рекламы

            break;

        case 'pl': // загрузка плейлиста

            break;

        case 'volume': // изменение громкости

            break;
        default : break;
    }

}

// команды - http://uppod.ru/player/js#send

function uppodSend(playerID,com,callback) {
    document.getElementById(playerID).sendToUppod(com);
}

// запросы - http://uppod.ru/player/js#get

function uppodGet(playerID,com,callback) {
    return document.getElementById(playerID).getUppod(com);
}


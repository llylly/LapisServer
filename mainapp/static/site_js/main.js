/**
 * Created by lly on 11/11/2017.
 */

var editor = null;
session = "-1";

datagen_cpystr = "";
singleapi_cpystr = "";
scenario_cpystr = "";

function clean() {
    $('.parse_status_fin').removeClass('parse_status_fin').addClass('parse_status');
    $('.parse_status_err').removeClass('parse_status_err').addClass('parse_status');
    $('#error_panel').hide();
    $('#error_list').html("No error.");
    $('#api_list').html("");
    $('#scenario_list').html("");
    $('#api_ops').hide();
    $('#api_select').empty().append($("<option>").val('default').text('Select an API'));
    $('#scenario_ops').hide();
    $('#ali_secret_div').hide();
    $('#datagen_panel').hide();
    $('#singleapi_panel').hide();
    $('#scenario_running_div').hide();
    $('#scenario_notstart_div').hide();
    $('#scenario_finish_div').hide();
    $('#scenario-panel').hide();
    $('#scenario_running_updatestat').text('Not updated.');
    $('#change_div').hide();
}

$(function(){

    ticker();

    clean();

    editor = ace.edit("script_area");
    editor.setTheme("ace/theme/monokai");
    editor.getSession().setMode("ace/mode/yaml");

    editor.getSession().on('change', function(e) {
        if (session != "-1")
                $('#change_div').show();
    });
    $('#YAML-radio').change(function() {
        if (session != "-1")
            $('#change_div').show();
    });
    $('#XML-radio').change(function() {
        if (session != "-1")
            $('#change_div').show();
    });

    $('#YAML-radio').change(function(){
        if ($('#YAML-radio').is(':checked'))
            editor.getSession().setMode("ace/mode/yaml");
    });
    $('#XML-radio').change(function(){
        if ($('#XML-radio').is(':checked'))
            editor.getSession().setMode("ace/mode/xml");
    });

    $('#isali_checkbox').change(function(){
        if ($('#isali_checkbox').is(':checked')) {
            $('#ali_secret_div').show();
        } else {
            $('#ali_secret_div').hide();
        }
    });

    $('#datagen_copy').click(function(){
       $('#json_area').html(datagen_cpystr);
       $('#copy_modal').modal('show');
    });

    $('#singleapi_copy').click(function(){
       $('#json_area').html(singleapi_cpystr);
       $('#copy_modal').modal('show');
    });

    $('#scenario_copy').click(function(){
       $('#json_area').html(scenario_cpystr);
       $('#copy_modal').modal('show');
    });

    $('#file_btn').click(function(){
        if ($('#fileInput').prop('files').length <= 0) {
            alert('Please select a file.');
            return;
        }
        file = $('#fileInput').prop('files')[0];
        var formData = new FormData();
        formData.append("script", file);
        $.ajax({
            url: '/index_fileupload',
            type: 'POST',
            cache: false,
            data: formData,
            processData: false,
            contentType: false
        }).done(function(res) {
            res = eval(res);
            if (res.code != "200") {
                alert(res.msg);
            } else {
                editor.setValue(res.script);
            }
        }).fail(function(res) {
            alert('File upload failed.')
        });
    });

    $('#parse_btn').click(function(){

        clean();

        $.get(
            "/api/session_verify?id=" + session,
            function(data, status) {
                if (status != 'success') {
                    alert('Unknown Error');
                } else {
                    data = eval(data);
                    if (data.code != '200') {
                        alert('Unknown Error');
                    } else {
                        session = data.id;
                        type_str = '';
                        if ($('#YAML-radio').is(':checked'))
                            type_str = 'YAML';
                        if ($('#XML-radio').is(':checked'))
                            type_str = 'XML';
                        $.post(
                            '/api/script_parse',
                            {
                                'session': session,
                                'type': type_str,
                                'text': editor.getValue()
                            },
                            function(data, status) {
                                if (status != 'success') {
                                    alert('Unknown Error');
                                } else {
                                    if (data.code != '200') {
                                        alert('Unknown Error');
                                    }
                                    data = eval(data);
                                    result = data.result;
                                    if (result.docParse)
                                        $("#doc_status").removeClass("parse_status").addClass("parse_status_fin");
                                    else
                                        $("#doc_status").removeClass("parse_status").addClass("parse_status_err");
                                    if (result.docParse)
                                        if (result.apiParse)
                                            $("#api_status").removeClass("parse_status").addClass("parse_status_fin");
                                        else
                                            $("#api_status").removeClass("parse_status").addClass("parse_status_err");
                                    if (result.docParse && result.apiParse)
                                        if (result.scenarioParse)
                                            $("#scenario_status").removeClass("parse_status").addClass("parse_status_fin");
                                        else
                                            $("#scenario_status").removeClass("parse_status").addClass("parse_status_err");
                                    if (result.docParse && result.apiParse && result.scenarioParse)
                                        if (result.configParse)
                                            $("#config_status").removeClass("parse_status").addClass("parse_status_fin");
                                        else
                                            $("#config_status").removeClass("parse_status").addClass("parse_status_err");
                                    if (!result.docParse || !result.apiParse || !result.scenarioParse || !result.configParse) {
                                        $('#error_panel').show();
                                        error_arr = result.errors;
                                        error_str = "";
                                        for (index in error_arr) {
                                            now_item = error_arr[index];
                                            error_str += "<p>" + "line: " + now_item.line + "   " +
                                                "col: " + now_item.col + "<br>" +
                                                "errNo: " + now_item.errno + "<br>" +
                                                "msg: " + now_item.msg + "</p>";
                                        }
                                        $('#error_list').html(error_str);
                                    }
                                    if (result.apiParse) {
                                        api_str = "";
                                        for (index in result.apiNames) {
                                            now_item = result.apiNames[index];
                                            api_str += now_item.name + "  <span class=\"badge badge-success\">" +
                                                now_item.method + "</span><br>";
                                        }
                                        $('#api_list').html(api_str);
                                    }
                                    if (result.scenarioParse) {
                                        scenario_str = "";
                                        for (index in result.scenarioNames) {
                                            now_item = result.scenarioNames[index];
                                            scenario_str += String(now_item) + "<br>";
                                        }
                                        $("#scenario_list").html(scenario_str);
                                    }
                                    if (result.docParse && result.apiParse) {
                                        for (index in result.apiNames) {
                                            now_item = result.apiNames[index];
                                            text = '[' + now_item.method + '] ' + now_item.name;
                                            val = now_item.method + '_' + now_item.name;
                                            $("#api_select").append($("<option>").val(val).text(text));
                                        }
                                        $("#api_ops").show();
                                    }
                                    if (result.docParse && result.apiParse && result.scenarioParse && result.configParse) {
                                        $("#scenario_ops").show();
                                    }
                                }
                            }
                        );
                    }
                }
            }
        );
    });

    $('#datagen_btn').click(function(){
        if ($('#datagen_btn').attr("disabled") == "disabled") return;
        api_str = $("#api_select").val();
        index = api_str.indexOf('_');
        if (index == -1) {
            alert('Please specify an API.');
            return;
        }
        method = api_str.substr(0, index);
        api_name = api_str.substr(index + 1);


        $.get(
            "/api/session_verify?id=" + session,
            function(data, status) {
                if (status != 'success') {
                    alert('Unknown error.');
                } else {
                    data = eval(data);
                    if (data.code != '200') {
                        alert('Unknown error.');
                    } else {
                        session = data.id;
                        $('#datagen_btn').attr('disabled', 'disabled');
                        $.post(
                            "/api/apidata_gen",
                            {
                                session: session,
                                method: method,
                                api: api_name
                            },
                            function(data, status) {
                                $('#datagen_btn').removeAttr('disabled');
                                if (status != 'success') {
                                    alert('Unknown Error');
                                } else {
                                    data = eval(data);
                                    if (data.code == '203') {
                                        alert(data.msg);
                                        clean();
                                    } else if (data.code != '200') {
                                        alert(data.msg)
                                    } else {
                                        $('#datagen_panel').show();
                                        result = data.result;
                                        if ((result.succeed) && (result.errors.length == 0)) {
                                            $('#datagen_success_div').show();
                                            $('#datagen_fail_div').hide();
                                            datagen_cpystr = JSON.stringify(result.data);
                                            $('#datagen_div').html(present(result.data, 'datagen_res_', 0, 0).text);
                                        } else {
                                            $('#datagen_success_div').hide();
                                            $('#datagen_fail_div').show();
                                            $('#datagen_err_div').html(present(result.errors, 'datagen_errres_', 0, 0).text);
                                        }
                                    }
                                }
                            }
                        )
                    }
                }
            }
        );
    });

    $('#single_btn').click(function(){
        if ($('#single_btn').attr("disabled") == "disabled") return;
        api_str = $("#api_select").val();
        index = api_str.indexOf('_');
        if (index == -1) {
            alert('Please specify an API.');
            return;
        }
        method = api_str.substr(0, index);
        api_name = api_str.substr(index + 1);
        isali = $('#isali_checkbox').is(':checked');
        secret_key = $('#secretkey_text').val();
        if (isali) {
            if (secret_key == "")
                alert('Please specify Ali secret key.');
        }
        timeout = parseInt($('#timeout_input').val());
        if (isNaN(timeout) || (timeout <= 0)) {
            alert('Invalid timeout parameter. It should be a positive integer')
        }

        $.get(
            "/api/session_verify?id=" + session,
            function(data, status) {
                if (status != 'success') {
                    alert('Unknown error.');
                } else {
                    data = eval(data);
                    if (data.code != "200") {
                        alert('Unknown error.');
                    } else {
                        session = data.id;
                        $('#single_btn').attr('disabled', 'disabled');
                        $.post(
                            "/api/single_test",
                            {
                                session: session,
                                method: method,
                                api: api_name,
                                isali: isali,
                                secret_key: secret_key,
                                timeout: timeout
                            },
                            function(data, status) {
                                $('#single_btn').removeAttr('disabled');
                                if (status != 'success') {
                                    alert('Unknown Error');
                                } else {
                                    data = eval(data);
                                    if (data.code == '203') {
                                        alert(data.msg);
                                        clean();
                                    } else if (data.code != '200') {
                                        alert(data.msg)
                                    } else {
                                        $('#singleapi_panel').show();
                                        result = data.result;
                                        if ((result.succeed) && (result.errors.length == 0)) {
                                            $('#singleapi_success_div').show();
                                            $('#singleapi_fail_div').hide();
                                            singleapi_cpystr = JSON.stringify(result.report);
                                            $('#singleapi_div').html(present(result.report, 'singleapi_rep_', 0, 0).text);
                                        } else {
                                            $('#datagen_success_div').hide();
                                            $('#datagen_fail_div').show();
                                            $('#datagen_err_div').html(present(result.errors, 'singleapi_errres_', 0, 0).text);
                                        }
                                    }
                                }
                            }
                        )
                    }
                }
            }
        )
    });

    $('#scenario_btn').click(function(){
        if ($('#scenario_btn').attr("disabled") == "disabled") return;
        $.get(
            "/api/session_verify?id=" + session,
            function(data, status) {
                if (status != 'success') {
                    alert('Unknown error.');
                } else {
                    data = eval(data);
                    if (data.code != "200") {
                        alert('Unknown error.');
                    } else {
                        session = data.id;
                        $('#scenario_btn').attr('disabled', 'disabled');
                        $.post(
                            "/api/scenario_test",
                            {
                                session: session
                            },
                            function (data, status) {
                                if (status != 'success') {
                                    alert('Unknown Error');
                                    $('#scenario_btn').removeAttr('disabled');
                                } else {
                                    data = eval(data);
                                    if (data.code == '203') {
                                        alert(data.msg);
                                        clean();
                                        $('#scenario_btn').removeAttr('disabled');
                                    } else if (data.code != '200') {
                                        alert(data.msg)
                                        $('#scenario_btn').removeAttr('disabled');
                                    } else {
                                        $('#scenario-panel').show();
                                        $('#scenario_running_div').show();
                                        scenario_result_update();
                                    }
                                }
                            }
                        );
                    }
                }
            }
        );
    });

});

function ticker() {
    text = $('#scenario_running_updatestat').text();
    if (text == 'Updated just now.')
        $('#scenario_running_updatestat').text('Updated 1 second(s) ago.');

    if (text.indexOf(' second(s) ago') >= 0) {
        tail = text.indexOf(' second(s) ago');
        prev = text.substr(8, tail-8);
        prev = parseInt(prev);
        now = prev + 1;
        $('#scenario_running_updatestat').text('Updated ' + String(now) + ' second(s) ago.');
    }

    setTimeout(ticker, 1000);
}

function scenario_result_update() {
    $('#scenario_running_updatestat').text('Updated just now.');
    $.post(
        "/api/scenario_test_query",
        {
            session: session
        },
        function (data, status) {
            if (status != 'success') {
                alert('Unknown Error');
                $('#scenario_btn').removeAttr('disabled');
            } else {
                data = eval(data);
                if (data.code != '200') {
                    alert(data.msg);
                    $('#scenario_btn').removeAttr('disabled');
                } else {
                    if (data.stat == '-1') {
                        $('#scenario_notstart_div').show();
                        $('#scenario_running_div').hide();
                        $('#scenario_finish_div').hide();
                        $('#scenario_running_updatestat').text('Not updated.');
                        $('#scenario_btn').removeAttr('disabled');
                    }
                    if (data.stat == '0') {
                        $('#scenario_notstart_div').hide();
                        $('#scenario_running_div').show();
                        $('#scenario_finish_div').hide();
                        $('#case_num').text(data.caseN);
                        $('#step_num').text(data.stepN);
                        setTimeout(scenario_result_update, 3000);
                    }
                    if (data.stat == '1') {
                        $('#scenario_notstart_div').hide();
                        $('#scenario_running_div').hide();
                        $('#scenario_finish_div').show();
                        $('#scenario_div').html(present(data.result, 'scenario_rep_', 0, 0).text);
                        $('#scenario_btn').removeAttr('disabled');
                        scenario_cpystr = JSON.stringify(data.result);
                    }
                }
            }
        }
    )
}

function present(obj, idprefix, level, index) {

    function isArrayFn(value){
        if (typeof Array.isArray === "function") {
            return Array.isArray(value);
        }else{
            return Object.prototype.toString.call(value) === "[object Array]";
        }
    }

    function indent(level) {
        s = "";
        for (i=0; i<level; ++i)
            s += "&nbsp;&nbsp;";
        return s;
    }

    if (typeof(obj) == 'object') {
        var s = "";
        if (isArrayFn(obj)) {
            id_name = idprefix + String(index);
            s = "<span class='btn-link' data-toggle='collapse' data-target='#" + id_name + "'>Array</span>";
            s += "<div id='" + id_name + "' class='collapse'>";
            ++index;
            for (i in obj) {
                now_obj = obj[i];
                pre_item = present(now_obj, idprefix, level + 1, index);
                s += "<div>" + indent(level + 1) + "- " + pre_item.text + "</div>";
                index = pre_item.index;
            }
            s += "</div>";
        } else {
            id_name = idprefix + String(index);
            s = "<span class='btn-link' data-toggle='collapse' data-target='#" + id_name + "'>Object</span>";
            s += "<div id='" + id_name + "' class='collapse'>";
            ++index;
            for (key in obj) {
                var now_key = key;
                now_obj = obj[now_key];
                pre_item = present(now_obj, idprefix, level + 1, index);
                s += "<div>" + indent(level + 1) + now_key + ": " + pre_item.text + "</div>";
                index = pre_item.index;
            }
            s += "</div>";
        }
        return {text: s, index: index + 1};
    } else {
        var s = "<span id='" + idprefix + String(index) + "'>" + JSON.stringify(obj) + "</span>";
        return {text: s, index: index + 1};
    }
}



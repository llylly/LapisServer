/**
 * Created by lly on 11/11/2017.
 */

var editor = null;
session = "-1";

datagen_cpystr = "";
singleapi_cpystr = "";
scenario_cpystr = "";

change_flag = false;

function clean() {
    $('.parse_status_fin').removeClass('parse_status_fin').addClass('parse_status');
    $('.parse_status_err').removeClass('parse_status_err').addClass('parse_status');
    $('#error_panel').hide();
    $('#error_list').html("No error.");
    $('#transform_ops').hide();
    $('#basic_info_panel').hide();
    $('#api_panel').hide();
    $('#api_list').html("");
    $('#api_ops').hide();
    $('#api_select').empty().append($("<option>").val('default').text('Select an API'));
    $('#datagen_panel').hide();
    $('#change_div').hide();
}

function save() {
    if (username != null) {
        if (change_flag) {
            $.post(
                "/api/user/save_file",
                {
                    filename: $('#filename_span').html(),
                    script: editor.getValue()
                },
                function (data, status) {
                    if (status != 'success') {
                        alert('Unknown Error');
                    } else {
                        data = eval(data);
                        if (data.code != "200") {
                            alert(data.msg);
                        } else {
                            bar_update();
                            $('#filename_astar').hide();
                        }
                    }
                }
            );
        } else {
            alert('There is no change.');
        }
    }
}

$(function(){
    clean();

    $('#filename_astar').hide();

    $(document).keydown(function(e){
        if( e.ctrlKey  == true && e.keyCode == 83 ){
            save();
            return false;
        }
    });
    $('#save_btn').click(function() {
        save();
    });

    editor = ace.edit("script_area");
    editor.setTheme("ace/theme/xcode");
    editor.getSession().setMode("ace/mode/yaml");
    editor.setHighlightActiveLine(true);
    editor.getSession().setUseWrapMode(true);

    editor.getSession().on('change', function(e) {
        if (session != "-1")
                $('#change_div').show();
        $('#filename_astar').show();
        change_flag = true;
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

    $('#datagen_copy').click(function(){
       $('#json_area').html(datagen_cpystr);
       $('#copy_modal').modal('show');
    });

    $('#filename_span').click(function(){
        $('#chgfilename_modal').modal('show');
        $('#chgfilename_input').val($('#filename_span').html());
    });

    $('#new_file_trigger_btn').click(function(){
        $('#newfile_modal').modal('show');
        if (editor.getValue() != '') {
            $('#newfile_danger_div').show();
        } else {
            $('#newfile_danger_div').hide();
        }
        $('#newfile_input').val('Noname');
    });

    $('#newfile_btn').click(function() {
       if ($('#newfile_input').val() == '') {
           alert('Name should not be empty.');
           return;
       }
       $('#filename_span').html($('#newfile_input').val());
       editor.setValue("");
       $('#filename_astar').hide();
       change_flag = false;
       $('#newfile_modal').modal('hide');
    });

    $('#chgfilename_btn').click(function() {
        oldname = $('#filename_span').html();
        newname = $('#chgfilename_input').val();
        if (newname == "") {
            alert("New name should not be empty.");
            return;
        }
        $('#filename_span').html(newname);
        $('#chgfilename_modal').modal('hide');

        in_list = false;
        for (i in files)
            if (files[i] == oldname) {
                in_list = true;
                break;
            }

        if (in_list) {
            $.post(
                "/api/user/rename_file",
                {
                    oldname: oldname,
                    newname: newname
                },
                function(data, status) {
                    if (status != 'success') {
                        alert('Unknown Error');
                    } else {
                        data = eval(data);
                        if (data.code != "200") {
                            alert(data.msg);
                        } else {
                            bar_update();
                        }
                    }
                }
            );
        } else {
            $('#filename_astar').show();
            change_flag = true;
        }
    });

    $('#rename_btn').click(function() {
        newname = $('#rename_input').val();
        if (newname == "") {
            alert("New name should not be empty.");
            return;
        }
        name_tmp2 = newname;
        $.post(
            "/api/user/rename_file",
            {
                oldname: name_tmp1,
                newname: name_tmp2
            },
            function(data, status) {
                if (status != 'success') {
                    alert('Unknown Error');
                } else {
                    data = eval(data);
                    if (data.code != "200") {
                        alert(data.msg);
                    } else {
                        bar_update();
                        if (name_tmp1 == $('#filename_span').html())
                            $('#filename_span').html(name_tmp2);
                        $('#rename_modal').modal('hide');
                    }
                }
            }
        )
    });

    $('#delconfirm_btn').click(function() {
       $.post(
            "/api/user/del_file",
            {
                filename: name_tmp1
            },
            function(data, status) {
                if (status != 'success') {
                    alert('Unknown Error');
                } else {
                    data = eval(data);
                    if (data.code != "200") {
                        alert(data.msg);
                    } else {
                        bar_update();
                        $('#delconfirm_modal').modal('hide');
                    }
                }
            }
        )
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
                $('#filename_span').html(res.name);
                save();
                change_flag = false;
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
                                    if (!result.docParse || !result.apiParse) {
                                        $('#error_panel').show();
                                        error_arr = result.errors;
                                        error_str = "";
                                        min_line = -1;
                                        for (index in error_arr) {
                                            now_item = error_arr[index];
                                            error_str += "<p>" + "line: " + now_item.line + "   " +
                                                "col: " + now_item.col + "<br>" +
                                                "errNo: " + now_item.errno + "<br>" +
                                                "msg: " + now_item.msg + "</p>";
                                            if (min_line == -1)
                                                min_line = now_item.line;
                                            else
                                                min_line = min(min_line, now_item.line);
                                        }
                                        editor.gotoLine(min_line);
                                        $('#error_list').html(error_str);
                                    }
                                    if (result.apiParse) {
                                        $('#basic_info_table').html(basic_info_present(result));
                                        api_str = "";
                                        for (index in result.apiNames) {
                                            now_item = result.apiNames[index];
                                            api_str += api_detail_present(now_item.name, now_item.method,
                                                eval('result.apiDetail["' + now_item.name + '"]["' + now_item.method + '"]'), index, "api_detail_");
                                        }
                                        $('#api_list').html(api_str);

                                        $('#basic_info_panel').show();
                                        $('#api_panel').show();
                                    }
                                    if (result.docParse && result.apiParse) {
                                        for (index in result.apiNames) {
                                            now_item = result.apiNames[index];
                                            text = '[' + now_item.method + '] ' + now_item.name;
                                            val = now_item.method + '_' + now_item.name;
                                            $("#api_select").append($("<option>").val(val).text(text));
                                        }
                                        if ($('#YAML-radio').is(':checked')) {
                                            $('#transform_btn').text('Transform to XML Format');
                                        }
                                        if ($('#XML-radio').is(':checked')) {
                                            $('#transform_btn').text('Transform to YAML Format');
                                        }
                                        $("#api_ops").show();
                                        $("#transform_ops").show();
                                        editor.resize();
                                    }
                                }
                            }
                        );
                    }
                }
            }
        );
    });

    $('#transform_btn').click(function(){
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
                        $.post(
                            "/api/script_transform",
                            {
                                session: session
                            },
                            function(data, status) {
                                if (status != 'success') {
                                    alert('Unknown Error');
                                } else {
                                    data = eval(data);
                                    if (data.code != "200") {
                                        alert(data.msg);
                                    } else {
                                        window.open(data.link, 'Download');
                                    }
                                }
                            }
                        )
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
                                            $('#datagen_div').html("&nbsp; &nbsp;" + present(result.data, 'datagen_res_', 2, 0).text);
                                        } else {
                                            $('#datagen_success_div').hide();
                                            $('#datagen_fail_div').show();
                                            $('#datagen_err_div').html(present(result.errors, 'datagen_errres_', 2, 0).text);
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

});

function basic_info_present(obj) {
    function arrSerailize(obj) {
        s = '';
        for (i in obj)
            s += obj[i] + '; ';
        return s;
    }

    function add(s, key, value) {
        return s + '<tr><td><strong>' + key + '</strong></td><td>' + value + '</td></tr>';
    }

    ans = '';
    ans = add(ans, 'Title', obj.info.title);
    if (!obj.info.description == false)
        ans = add(ans, 'Description', obj.info.description);
    else
        ans = add(ans, 'Description', '<em>Unfilled</em>');
    ans = add(ans, 'Version', obj.info.version);

    ans = add(ans, 'Host', obj.host);

    if (!obj.basePath == false)
        ans = add(ans, 'BasePath', obj.basePath);
    else
        ans = add(ans, 'BasePath', '<em>Unfilled</em>');

    if (!obj.schemes == false) {
        ans = add(ans, 'Schemes', arrSerailize(obj.schemes));
    } else
        ans = add(ans, 'Schemes', '<em>Unfilled</em>');

    if (!obj.consumes == false) {
        ans = add(ans, 'Consumes', arrSerailize(obj.consumes));
    } else
        ans = add(ans, 'Consumes', '<em>Unfilled</em>');

    if (!obj.produces == false) {
        ans = add(ans, 'Produces', arrSerailize(obj.produces))
    } else
        ans = add(ans, 'Produces', '<em>Unfilled</em>');

    return ans;
}

function api_detail_present(name, method, entity, no, prefix) {
    tag_str = '';
    if (!entity.tags == false) {
        tag_str = '<tr>\
        <td>Tags</td>\
        <td>';
        for (ind in entity.tags) {
            tag_str += '<span class="badge badge-default">' + entity.tags[ind] + '</span>';
        }
        tag_str += '</td></tr>';
    }

    summary_str = '';
    if (!entity.summary == false)
        summary_str = entity.summary;

    description_str = '';
    if (!entity.description == false)
        description_str = entity.description;

    externaldoc_str = '';
    if (!entity.externalDocs == false)  {
        externaldoc_str = '<tr><td>ExternalDocs</td><td>' + present(entity.externalDocs, prefix + 'external_doc_', 0, 0).text + '</td></tr>';
    }

    operationid_str = '';
    if (!entity.operationId == false) {
        operationid_str = '<tr><td>OperationId</td><td>' + entity.operationId + '</td></tr>';
    }

    consumes_str = '';
    for (ind in entity.consumes) {
        consumes_str += entity.consumes[ind] + '; ';
    }

    produces_str = '';
    for (ind in entity.produces) {
        produces_str += entity.produces[ind] + '; ';
    }

    schemes_str = '';
    for (ind in entity.schemes) {
        schemes_str += entity.schemes[ind] + '; ';
    }

    deprecated_str = '';
    if (entity.deprecated) {
        deprecated_str = '<tr><td><span class="text-error">Deprecated</span></td><td><span class="text-error">True</span></td></tr>';
    }

    constraint_str = '';
    if (!entity['x-constraint'] == false) {
        constraint_str = '<tr><td>x-constraint</td><td>' + present(entity['x-constraint'], prefix + 'constraint_', 0, 0).text + '</td></tr>';
    }

    // --------

    param_str = '<table class="table"><thead><tr><th>Name</th><th>In</th><th>Required</th><th>Description</th><th>Schema</th></tr></thead><tbody>';
    has_param = false;
    for (i in entity.parameters) {
        has_param = true;
        now_param = entity.parameters[i];
        param_str += '<tr><td>' + now_param.name + '</td><td>'  + now_param.in + '</td>' + '<td>';
        param_str += now_param.required;
        if (!now_param['x-nullProbability'] == false) {
            param_str += ' (NullProbability = ' + String(now_param['x-nullProbability']) + ')';
        }
        param_str += '</td><td>';
        if (!now_param.description == false)
            param_str += now_param.description;
        param_str += '</td><td>';
        if (!now_param['schema'] == false)
            param_str += present(now_param['schema'], prefix + 'param_' + String(i) + '_schema_', 0, 0).text;
        if (!now_param['x-schema'] == false)
            param_str += present(now_param['x-schema'], prefix + 'param_' + String(i) + '_schema_', 0, 0).text;
        param_str += '</td></tr>';
    }
    if (!has_param) param_str += '<tr><td>No Parameter</td></tr>';
    param_str += '</tbody></table>';

    // --------

    response_str = '<table class="table"><thead><tr><th>Code</th><th>Description</th><th>Schema</th></tr></thead><tbody>';
    has_resp = false;
    for (key in entity.responses)
        if (key != 'x-extension') {
            has_resp = true;
            now_resp = entity.responses[key];
            response_str += '<tr><td>' + key + '</td><td>';
            if (!now_resp.description == false)
                response_str += now_resp.description;
            response_str += '</td><td>';
            if (!now_resp.schema == false)
                response_str += present(now_resp.schema, prefix + 'response_' + String(i) + '_schema_', 0, 0).text;
            response_str += '</td></tr>';
        }
    if (!has_resp) response_str += '<tr><td>No Response Definition</td></tr>';
    response_str += '</tbody></table>';

    // --------

    responseext_str = '';
    if (!entity.responses['x-extension'] == false) {
        inner_str = '<table class="table"><thead><tr><th>Code</th><th>Name</th><th>Description</th><th>Field</th><th>Schema</th><th>Related Parameters</th></tr></thead><tbody>';
        has_ext = false;
        for (i in entity.responses['x-extension']) {
            has_ext = true;
            now_ext = entity.responses['x-extension'][i];
            inner_str += '<tr><td>' + now_ext.code + '</td>';
            inner_str += '<td>' + now_ext.name + '</td>';
            inner_str += '<td>';
            if (!now_ext.description == false)
                inner_str += now_ext.description;
            inner_str += '</td>';
            inner_str += '<td>' + now_ext.field + "</td>";
            inner_str += '<td>';
            if (!now_ext.schema == false)
                inner_str += present(now_ext.schema, prefix + 'responseext_' + String(i) + '_schema_', 0, 0).text;
            inner_str += '</td>';
            inner_str += '<td>';
            for (j in now_ext.relatedParameters) {
                inner_str += now_ext.relatedParameters[j] + '; ';
            }
            inner_str += '</td></tr>';
        }
        if (!has_ext) inner_str += '<tr><td>No Response Extension Definition.</td></tr>';
        inner_str += '</tbody></table>';
        responseext_str = '<div class="panel panel-info">\
                       <div class="panel-heading" style="font-size: 10pt">\
                           <a href="#" data-toggle="collapse" data-target="#' + prefix + String(no) + '_responseext' + '">Response Extensions</a>\
                   </div>\
                   <div class="panel-body collapse" id="' + prefix + String(no) + '_responseext' + '">' + inner_str + '</div>\
               </div>';
    }

    // --------

    ans = '<div class="panel panel-success">\
           <div class="panel-heading" style="font-size: 12pt">\
              <a data-toggle="collapse" href="#" data-target="#' + prefix + String(no) + '">' + name + '</a>\
               <span class="badge badge-info">' + method + '</span>\
               &nbsp; &nbsp; <h6 style="display: inline">' + summary_str + '</h6>\
           </div>\
           <div class="panel-body collapse" id="' + prefix + String(no) + '">\
               <table class="table">\
                   <thead />\
                   <tbody>' +
        tag_str +
                       '<tr>\
                           <td>Description</td>\
                           <td>' + description_str + '</td>\
                       </tr>' +
        externaldoc_str +
        operationid_str +
                       '<tr>\
                           <td>Consumes</td>\
                           <td>' + consumes_str + '</td>\
                       </tr>\
                       <tr>\
                           <td>Produces</td>\
                           <td>' + produces_str + '</td>\
                       </tr>\
                       <tr>\
                           <td>Schemes</td>\
                           <td>' + schemes_str + '</td>\
                       </tr>' +
        deprecated_str +
        constraint_str +
                   '</tbody>\
               </table>\
               <div class="panel panel-info">\
                   <div class="panel-heading" style="font-size: 10pt">\
                       <a href="#" data-toggle="collapse" data-target="#' + prefix + String(no) + '_param' + '">Parameters</a>\
                   </div>\
                   <div class="panel-body collapse" id="' + prefix + String(no) + '_param' + '">' + param_str + '</div>\
               </div>\
               <div class="panel panel-info">\
                   <div class="panel-heading" style="font-size: 10pt">\
                       <a href="#" data-toggle="collapse" data-target="#' + prefix + String(no) + '_response' + '">Responses</a>\
                   </div>\
                   <div class="panel-body collapse" id="' + prefix + String(no) + '_response' + '">' + response_str + '</div>\
               </div>' +
        responseext_str +
           '</div>\
        </div>';
    return ans;
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



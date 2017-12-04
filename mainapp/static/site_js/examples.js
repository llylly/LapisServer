/**
 * Created by lly on 28/11/2017.
 */

example = null;
var vEditor = null, sEditor = null;

$(function(){
    $.post(
        '/get_cloud_api_examples',
        {},
        function(data, status) {
            if (status != 'success') {
                alert('Unknown Error');
            } else {
                data = eval(data);
                example = data.result;
                $('#cloud_example_list').html(load_example(example, 0, 0).text);
                refresh_loadlink();
            }
        }
    );

    vEditor = ace.edit("example_view_area");
    vEditor.setTheme("ace/theme/xcode");
    vEditor.getSession().setMode("ace/mode/yaml");
    vEditor.setHighlightActiveLine(true);
    vEditor.getSession().setUseWrapMode(true);
    vEditor.setReadOnly(true);

    sEditor = ace.edit("example_sup_area");
    sEditor.setTheme("ace/theme/xcode");
    sEditor.getSession().setMode("ace/mode/yaml");
    sEditor.setHighlightActiveLine(true);
    sEditor.getSession().setUseWrapMode(true);
    sEditor.setReadOnly(true);
});

function refresh_loadlink() {
    $(".load_example").click(function() {
        $.get(
            "/read_cloud_api_examples?path=" + $(this).data('path'),
            function(data, status) {
                if (status != 'success') {
                    alert('Unknown Error');
                } else {
                    data = eval(data);
                    if (data.code != '200')
                        alert(data.msg);
                    else {
                        $("#example_name_div").html(data.path);
                        vEditor.setValue(data.script, 1);
                        if (data.format == 'yaml')
                            vEditor.getSession().setMode("ace/mode/yaml");
                        if (data.format == 'xml')
                            vEditor.getSession().setMode("ace/mode/xml");
                        if (data.format == 'md')
                            vEditor.getSession().setMode("ace/mode/yaml");
                        sEditor.setValue(data.supplement, 1);
                    }
                }
            }
        )
    });
}

function load_example(obj, indent, index) {
    function get_indent(level) {
        s = '';
        for (i=0; i<level; ++i)
            s += '&nbsp; &nbsp;';
        return s;
    }

    var ans = '';
    var son_dir = obj.sondir;
    for (key in son_dir) {
        if (typeof(son_dir[key]) == 'object') {
            compress = '';
            if ('compress' in son_dir[key])
                compress = '&nbsp;<a class="pull-right" href="/download_cloud_api_examples?path=' + son_dir[key].compress + '">' + '[Download]' + '</a>';
            ++index;
            ans += get_indent(indent) + '<i class="icon-th-list"></i>&nbsp;' + '<span class="btn-link" data-toggle="collapse" data-target="#example_' + String(index) + '">' + key+ '</span>'+ compress;
            ans += '<div id="example_' + String(index) + '" class="collapse">';
            tmp = load_example(son_dir[key], indent + 1, index);
            ans += tmp.text;
            ans += '</div>';
            index = tmp.index;
        } else {
            ans += get_indent(indent) + '<a class="btn-link load_example" href="#" data-path="'+ son_dir[key] + '">' + key + '</a>' +
                '&nbsp;<a class="pull-right" href="/download_cloud_api_examples?path=' + son_dir[key] + '">' + '[Download]' + '</a><br>';
        }

    }

    /*
    if (typeof(obj) == 'object') {
        for (key in obj) {
            key_str = get_indent(indent) + key;
            if (typeof(obj[key]) == 'object') {
                ans += '<tr><td>' + key_str + '</td><td></td></tr>';
                ans += load_example(obj[key], indent + 1)
            } else {
                ans += '<tr><td>' + key_str + '</td><td><a href="/download_cloud_api_examples?path=' + obj[key] + '">Download</a>' + '</td></tr>';
            }
        }
    } else {
        ans += '<tr><td><a href="/download_cloud_api_examples?path=' + obj + '">Download</a>' + '</td></tr>';
    }
    */
    return {'text': ans, 'index': index};
}
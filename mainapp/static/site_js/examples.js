/**
 * Created by lly on 28/11/2017.
 */

example = null;
var yamlEditor = null, xmlEditor = null, mdEditor = null;
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

    yamlEditor = ace.edit("yaml_content");
    yamlEditor.setTheme("ace/theme/xcode");
    yamlEditor.getSession().setMode("ace/mode/yaml");
    yamlEditor.setHighlightActiveLine(true);
    yamlEditor.getSession().setUseWrapMode(true);
    yamlEditor.setReadOnly(true);

    xmlEditor = ace.edit("xml_content");
    xmlEditor.setTheme("ace/theme/xcode");
    xmlEditor.getSession().setMode("ace/mode/xml");
    xmlEditor.setHighlightActiveLine(true);
    xmlEditor.getSession().setUseWrapMode(true);
    xmlEditor.setReadOnly(true);

    mdEditor = ace.edit("md_content");
    mdEditor.setTheme("ace/theme/xcode");
    mdEditor.getSession().setMode("ace/mode/yaml");
    mdEditor.setHighlightActiveLine(true);
    mdEditor.getSession().setUseWrapMode(true);
    mdEditor.setReadOnly(true);

    yamlEditor.setShowPrintMargin(false);
    xmlEditor.setShowPrintMargin(false);
    mdEditor.setShowPrintMargin(false);

    // vEditor = ace.edit("example_view_area");
    // vEditor.setTheme("ace/theme/xcode");
    // vEditor.getSession().setMode("ace/mode/yaml");
    // vEditor.setHighlightActiveLine(true);
    // vEditor.getSession().setUseWrapMode(true);
    // vEditor.setReadOnly(true);
    //
    // sEditor = ace.edit("example_sup_area");
    // sEditor.setTheme("ace/theme/xcode");
    // sEditor.getSession().setMode("ace/mode/yaml");
    // sEditor.setHighlightActiveLine(true);
    // sEditor.getSession().setUseWrapMode(true);
    // sEditor.setReadOnly(true);

    $('#yaml_tab').removeClass('active').hide();
    $('#xml_tab').removeClass('active').hide();
    $('#md_tab').removeClass('active').hide();
    $('#yaml_content').removeClass('active').addClass('fade');
    $('#xml_content').removeClass('active').addClass('fade');
    $('#md_content').removeClass('active').addClass('fade');

    $('.codetabs').click(function() {
        func = function() {
            yamlEditor.resize();
            xmlEditor.resize();
            mdEditor.resize();
        };
        setTimeout(func, 10);
    })
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

                        $('#yaml_tab').removeClass('active').hide();
                        $('#xml_tab').removeClass('active').hide();
                        $('#md_tab').removeClass('active').hide();
                        $('#yaml_content').removeClass('active').addClass('fade');
                        $('#xml_content').removeClass('active').addClass('fade');
                        $('#md_content').removeClass('active').addClass('fade');

                        avail = '';

                        if ('yaml' in data) {
                            if (avail == '') avail = 'yaml';
                            yamlEditor.getSession().setValue(data.yaml);
                            $('#yaml_tab').show();
                            $('#yaml_content').removeClass('fade');
                        }
                        if ('xml' in data) {
                            if (avail == '') avail = 'xml';
                            xmlEditor.getSession().setValue(data.xml);
                            $('#xml_tab').show();
                            $('#xml_content').removeClass('fade');
                        }
                        if ('md' in data) {
                            if (avail == '') avail = 'md';
                            mdEditor.getSession().setValue(data.md);
                            $('#md_tab').show();
                            $('#md_content').removeClass('fade');
                        }

                        if (avail == 'yaml') {
                            $('#yaml_tab').addClass('active');
                            $('#yaml_content').addClass('active');
                        }
                        if (avail == 'xml') {
                            $('#xml_tab').addClass('active');
                            $('#xml_content').addClass('active');
                        }
                        if (avail == 'md') {
                            $('#md_tab').addClass('active');
                            $('#md_content').addClass('active');
                        }

                        // vEditor.setValue(data.script, 1);
                        // if (data.format == 'yaml')
                        //     vEditor.getSession().setMode("ace/mode/yaml");
                        // if (data.format == 'xml')
                        //     vEditor.getSession().setMode("ace/mode/xml");
                        // if (data.format == 'md')
                        //     vEditor.getSession().setMode("ace/mode/yaml");
                        // sEditor.setValue(data.supplement, 1);
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
        compress = '';
        if ('compress' in son_dir[key])
            compress = '&nbsp;<a class="pull-right" href="/download_cloud_api_examples?path=' + son_dir[key].compress + '">' + '[下载]' + '</a>';

        if (!son_dir[key].file) {
            ++index;
            ans += '<div>' + get_indent(indent) + '<i class="icon-th-list"></i>&nbsp;' +
                '<a class="btn-link load_example" href="#" data-toggle="collapse" data-path="'+ son_dir[key].name + '"data-target="#example_' + String(index) + '">' + key+ '</a>'+ compress
                + '</div>';
            ans += '<div id="example_' + String(index) + '" class="collapse">';
            tmp = load_example(son_dir[key], indent + 1, index);
            ans += tmp.text;
            ans += '</div>';
            index = tmp.index;
        } else {
            ans += '<div>' + get_indent(indent) + '<a class="btn-link load_example" href="#" data-path="'+ son_dir[key].name + '">' + key + '</a>' + compress
                + '</div>';
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
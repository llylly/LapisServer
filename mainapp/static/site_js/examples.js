/**
 * Created by lly on 28/11/2017.
 */

example = null;

$(function(){
    $.post(
        '/get_cloud_api_examples',
        {},
        function(data, status) {
            if (status != 'success') {
                alert('Unknown Error');
            } else {
                example = data.result;
                $('#cloud_example_list').html(load_example(example, 0));
            }
        }
    )
});

function load_example(obj, indent) {
    function get_indent(level) {
        s = '';
        for (i=0; i<level; ++i)
            s += '&nbsp; &nbsp;';
        return s;
    }
    var ans = '';
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
    return ans;
}
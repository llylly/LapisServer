/**
 * Created by lly on 26/11/2017.
 */

username = null;
files = [];

var name_tmp1 = null;
var name_tmp2 = null;

$(function(){
    get_status();

    $('.dropdown-menu').click(function(e) {e.stopPropagation();});

    $('#register_btn').click(function() {

        username = $('#reg_username').val();
        passwd = $('#reg_password').val();
        passwd_repeat = $('#reg_password_repeat').val();

        if (username == "") {
            alert('Username should not be empty.');
            return;
        }
        if (passwd == "") {
            alert('Password should not be empty.');
            return;
        }
        if (passwd != passwd_repeat) {
            alert('Two passwords should be the same.');
            return;
        }
        passwd = $.md5(passwd);

        $.post(
            "/api/user/register",
            {
                username: username,
                passwd: passwd
            },
            function(data, status) {
                if (status != 'success') {
                    alert('Unknown Error');
                } else {
                    $('#reg_password').val("");
                    $('#reg_password_repeat').val("");
                    data = eval(data);
                    if (data.code != "200") {
                        alert(data.msg);
                    } else {
                        get_status();
                    }
                }
            }
        );

        $('#reg_dropdown').dropdown('toggle');
    });

    $('#login_btn').click(function() {

        username = $('#login_username').val();
        passwd = $('#login_password').val();

        if (username == "") {
            alert('Username should not be empty.');
            return;
        }
        if (passwd == "") {
            alert('Password should not be empty.');
            return;
        }
        passwd = $.md5(passwd);

        $.post(
            "/api/user/login",
            {
                username: username,
                passwd: passwd
            },
            function(data, status) {
                if (status != 'success') {
                    alert('Unknown Error');
                } else {
                    $('#login_password').val("");
                    data = eval(data);
                    if (data.code != "200") {
                        alert(data.msg);
                    } else {
                        get_status();
                    }
                }
            }
        );

        $('#login_dropdown').dropdown('toggle');
    });

    $('#logout_nav').click(function() {
        $.get(
            "/api/user/logout",
            function(data, status) {
                if (status != 'success') {
                    alert('Unknown Error');
                } else {
                    get_status();
                }
            }
        );
    });

    $('#delete_all_nav').click(function() {
        $('#delete_all_modal').modal('show');
    });

    $('#delete_all_btn').click(function() {
        $.post(
            '/api/user/clean_all',
            {},
            function(data, status) {
                if (status != 'success') {
                    alert('Unknown Error');
                } else {
                    data = eval(data);
                    if (data.code != '200') {
                        alert(data.msg);
                    }
                    $('#delete_all_modal').modal('hide');
                    get_status();
                }
            }
        );
    });

    $('#download_all_nav').click(function() {
        $.post(
            '/api/user/make_download_all',
            {},
            function(data, status) {
               if (status != 'success') {
                    alert('Unknown Error');
                } else {
                    data = eval(data);
                    if (data.code != '200') {
                        alert(data.msg);
                    }
                    $('#downloadallForm').submit();
                }
            }
        );
    });

    $('#changepwd_nav').click(function() {
        $('#changepasswd_modal').modal('show');
    });

    $('#changepwd_btn').click(function() {

        oldpasswd = $('#change_oldpwd').val();
        newpasswd = $('#change_newpwd').val();
        newpasswd1 = $('#change_newpwd_repeat').val();

        if (oldpasswd == "") {
            alert('Old password should not be empty.');
            return;
        }
        if (newpasswd == "") {
            alert('New password should not be empty.');
            return;
        }
        if (newpasswd != newpasswd1) {
            alert('Two new passwords should be the same.');
            return;
        }

        oldpasswd = $.md5(oldpasswd);
        newpasswd = $.md5(newpasswd);

        $.post(
            "/api/user/change_passwd",
            {
                old_passwd: oldpasswd,
                new_passwd: newpasswd
            },
            function(data, status) {
                if (status != 'success') {
                    alert('Unknown Error');
                } else {
                    $('#change_oldpwd').val("");
                    $('#change_newpwd').val("");
                    $('#change_newpwd_repeat').val("");
                    data = eval(data);
                    if (data.code != "200") {
                        alert(data.msg);
                    } else {
                        alert('Successfully changed.');
                        $("#changepasswd_modal").modal('hide');
                    }
                }
            }
        )
    });

    $('#filelist_search').keyup(function() {
        console.log($('#filelist_search').val());
        update_fileview();
    });
});

function get_status() {
    $.post(
        "/api/user/get_status",
        {},
        function(data, status) {
            if (status != 'success') {
                alert('Unknown Error');
            } else {
                data = eval(data);
                if (data.code == "200") {
                    username = data.username;
                } else {
                    username = null;
                }
                bar_update();
            }
        }
    )
}

function bar_update() {
    if (username == null) {
        $(".user_unlogin").show();
        $(".user_login").hide();
        $('.mainpage-filediv').hide();
        $("#filename_div").hide();
        $("#save_btn").hide();

        files = [];
    } else {
        $(".user_unlogin").hide();
        $(".user_login").show();
        $('.mainpage-filediv').show();
        $("#filename_div").show();
        $("#save_btn").show();
        $("#username_span").text(username);

        $.post(
            "/api/user/get_filelist",
            {},
            function(data, status) {
                if (status != 'success') {
                    alert('Unknown Error.');
                } else {
                    data = eval(data);
                    if (data.code == "200") {
                        files = data.result;
                        update_fileview();
                    } else {
                        alert(data.msg);
                    }
                }
            }
        )

    }
}

function update_fileview() {
    str = "";
    search_text = $('#filelist_search').val();
    for (i in files)
        if ((files[i].toLowerCase().indexOf(search_text.toLowerCase()) != -1) || (search_text == '')) {
            fname = files[i];
            str += '<div class="item">' +
                '<a href="#" class="fload" data-filename="' + fname + '">' + fname + '</a>' +
                '<a href="#" class="btn btn-small btn-danger pull-right fdelete" data-filename="' + fname + '">删除</a>' +
                '<a href="#" class="btn btn-small btn-primary pull-right frename" data-filename="' + fname + '">重命名</a></div>';
        }
    $(".mainpage-filelist").html(str);
    $('.mainpage-filediv .item .btn-small').hide();
    $('.mainpage-filediv .item').hover(
        function() {$(this).find('.btn-small').show(); $(this).css({'background-color': '#F5F5F5'});},
        function() {$(this).find('.btn-small').hide(); $(this).css({'background-color': 'white'});});


    $(".fload").click(function() {
        $('#waitDialog').modal('show');
        filename = $(this).data('filename');
        $.post(
            "/api/user/load_file",
            {
                filename: filename
            },
            function(data, status) {
                $('#waitDialog').modal('hide');
                if (status != 'success') {
                    alert('Unknown Error');
                } else {
                    data = eval(data);
                    if (data.code != "200") {
                        alert(data.msg);
                    } else {
                        $('#filename_span').html(filename);
                        editor.setValue(data.script);
                        $('#filename_astar').hide();
                        editor.resize();
                        realtime_transform();
                        change_flag = false;
                        bold_update();
                    }
                }
            }
        );
    });

    $(".fdelete").click(function() {
        name_tmp1 = $(this).data('filename');
        $('#delconfirm_filename').html(name_tmp1);
        $('#delconfirm_modal').modal('show');
    });

    $(".frename").click(function() {
        name_tmp1 = $(this).data('filename');
        $('#rename_input').val(name_tmp1);
        $('#rename_modal').modal('show');
    });

    bold_update();
}

function bold_update() {
    filename = $('#filename_span').html();
    len = $('.mainpage-filediv .item').length;
    for (i=0; i<len; ++i) {
        now = $('.mainpage-filediv .item')[i];
        if ($(now).find('.fload').data('filename') == filename) {
            $(now).css({'font-weight': 'bold'})
        } else {
            $(now).css({'font-weight': ''});
        }
    }
}

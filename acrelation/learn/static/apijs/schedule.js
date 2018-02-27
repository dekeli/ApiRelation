/**
 * Created by weiq on 17-8-11.
 */

$().ready(function(){
    menu_css($("#menu_schedule"));
    $("#pms_product").parent().css("display", "block");
    $('#scheduleTable').dataTable({
        "bPaginate": true,
        "bLengthChange": false,
        "iDisplayLength": 15,
        "bFilter": false,
        "bSort": true,
        "bInfo": true,
        "bAutoWidth": true,
        "oLanguage": {
            "sEmptyTable":"无相关记录"
        },
        "pagingType": "full_numbers",
        "bDestroy":true,
        "retrieve": true
    });
    $("#tqd").select2();
    $("#manager").select2();
    $("#new_erp").select2();
    $("#new_tqd").select2();
    $("#new_test_commit_time").datetimepicker({
        format: 'yyyy-mm-dd',
        weekStart: 1,
        todayBtn: 1,
        startView: 2,
        minView: 2,
        forceParse: false,
        language: 'zh-CN',
        autoclose: true
    });
    $("#new_release_time").datetimepicker({
        format: 'yyyy-mm-dd',
        weekStart: 1,
        todayBtn: 1,
        startView: 2,
        minView: 2,
        forceParse: false,
        language: 'zh-CN',
        autoclose: true
    });
    $("#api_doc_time").datetimepicker({
        format: 'yyyy-mm-dd',
        weekStart: 1,
        todayBtn: 1,
        startView: 2,
        minView: 2,
        forceParse: false,
        language: 'zh-CN',
        autoclose: true
    });
});
//一二级模块的关联
function change_pms_module(module_name){
    //初始化版本、服务、接口下拉
    for(var i=1;i<$("#product_name option").length;i++){
        $("#product_name option").eq(i).css("display", "none");
        $("#product_name option")[0].selected = true;
    }
    if(module_name != "0"){
        var obj = $("#product_name option[_pmsname=" + module_name + "]");
        for(var j=0;j<obj.length;j++){
            obj.eq(j).css("display", "block")
        }
    }
    search();
}
//新增修改弹框 一二级模块的关联
function change_pms_module_modal(module_name){
    //初始化版本、服务、接口下拉
    for(var i=1;i<$("#product_name_modal option").length;i++){
        $("#product_name_modal option").eq(i).css("display", "none");
        $("#product_name_modal option")[0].selected = true;
    }
    if(module_name != "0"){
        var obj = $("#product_name_modal option[_pmsname=" + module_name + "]");
        for(var j=0;j<obj.length;j++){
            obj.eq(j).css("display", "block")
        }
    }
}
//新增修改弹框 初始化一二级模块的关联
function change_product_name(module_name,product_id){
    //初始化版本、服务、接口下拉
    for(var i=1;i<$("#product_name_modal option").length;i++){
        $("#product_name_modal option").eq(i).css("display", "none");
        $("#product_name_modal option")[0].selected = true;
    }
    if(module_name != "0"){
        var obj = $("#product_name_modal option[_pmsname=" + module_name + "]");
        for(var j=0;j<obj.length;j++){
            obj.eq(j).css("display", "block")
        }
    }
    $("#product_name_modal").val(product_id);
}
//获取基本信息页的下拉菜单数据：组件、erp
//function get_schedule_init_data(){
//    $.ajax({
//        type: 'GET',
//        url : '/get_101_component/',
//        dataType : 'json',
//        success : function(data){
//            //初始化下拉菜单
//            $("#new_component").find("option").remove();
//            $("#new_component").append('<option value="0">请选择</option>');
//            for(var i=0;i<data.component_list.length;i++){
//                var option = '<option value="' + data.component_list[i].id + '">' + data.component_list[i].component_name + '</option>';
//                $("#new_component").append(option);
//            }
//            //成功后获取ERP数据
//            get_erp_items();
//        },
//        error: function(data){
//            if (data.responseJSON.message !== null && data.responseJSON.message !== undefined && data.responseJSON.message !== '') {
//                alert(data.responseJSON.message);
//            }else{
//                alert_msg("获取ERP项目列表失败");
//            }
//        }
//    });
//}

function get_erp_items(){
    $.ajax({
        type: 'GET',
        url : '/get_erp_items/',
        dataType : 'json',
        success : function(data){
            //初始化下拉菜单
            $("#new_erp").find("option").remove();
            $("#new_erp").append('<option value="0">请选择</option>');
            for(var i=0;i<data.erp_list.length;i++){
                var option = '<option value="' + data.erp_list[i].code + '">' + data.erp_list[i].name + '</option>';
                $("#new_erp").append(option);
            }
            $('#add_schedule_modal').modal('show');
            var modal_footer = $("#edit_add_modal_footer");
            $("#new_flow_name").val("");
            $("#new_flow_desc").val("");
            var button_close = $("<button type='button' class='btn btn-default' data-dismiss='modal'>关闭</button>");
            var button_save = $("<button type='button' onclick='add_schedule_confirm()' class='btn btn-primary'>保存</button>");
            $(modal_footer).empty()
                .append(button_close)
                .append(button_save);
        },
        error: function(data){
            if (data.responseJSON.message !== null && data.responseJSON.message !== undefined && data.responseJSON.message !== '') {
                alert(data.responseJSON.message);
            }else{
                alert("获取ERP项目列表失败");
            }
        }
    })
}

//新增版本进度
function add_schedule(){
    init_schedule_basic();
    get_erp_items();
}

function change_erp(){
    if($("#add_schedule_modal").attr("_e_init")=="false"){
        $("#new_tqd").select2("val", "0");
        $("#new_tqd").attr("disabled", true);
        $.ajax({
            type: 'GET',
            url : '/get_tqd_list/?code=' + $("#new_erp").val(),
            dataType : 'json',
            success : function(data){
                //初始化下拉菜单
                $("#new_tqd").find("option").remove();
                $("#new_tqd").append('<option value="0">请选择</option>');
                for(var i=0;i<data.tqd_list.items.length;i++){
                    var option = '<option value="' + data.tqd_list.items[i].id + '">' + "【" + data.tqd_list.items[i].id + "】" + data.tqd_list.items[i].title + '</option>';
                    $("#new_tqd").append(option);
                }
                $("#new_tqd").attr("disabled", false);
            },
            error: function(data){
                $("#new_tqd").attr("disabled", false);
                if (data.responseJSON.message !== null && data.responseJSON.message !== undefined && data.responseJSON.message !== '') {
                    alert(data.responseJSON.message);
                }else{
                    alert("获取TQD列表失败");
                }
            }
        })
    }
}

function change_tqd(obj){
    var tqd_full_text = $("#select2-new_tqd-container").text();
    if(tqd_full_text.length>27)
        $("#select2-new_tqd-container").text(tqd_full_text.substr(0,26) + "…");
}

function add_schedule_confirm(){
    if($("#pms_module_name_modal").val() == 0){
//        alert("组件名称不能为空")
        alert_msg("请选择一级模块哦~");
    }else if($("#product_name_modal").val() == 0){
        alert_msg("请选择二级模块哦~");
    }else if($("#new_version").val() == ""){
        alert_msg("版本不能为空");
    }else if($("#new_manager").val() == ""){
        alert_msg("负责人不能为空");
    }else if($("#new_tester").val() == ""){
        alert_msg("测试人员不能为空");
    }else if($("#new_test_commit_time").val() == ""){
        alert_msg("提测时间不能为空");
    }else if($("#new_release_time").val() == ""){
        alert_msg("发布时间不能为空");
    }else{
        var postData = {
            "component" : $("#product_name_modal").val(),
            "version" : $("#new_version").val(),
            "erp": $("#new_erp").val(),
            "tqd" : $("#new_tqd").val(),
            "manager" : $("#new_manager").val(),
            "tester" : $("#new_tester").val(),
            "test_commit_time" : $("#new_test_commit_time").val(),
            "release_time" : $("#new_release_time").val()
        };
        $.ajax({
            type: 'POST',
            url : '/schedule_add/',
            data : postData,
            dataType : 'json',
            success : function(data){
                if(data.result == "fail"){
                    alert("新增失败");
                }
                if(data.result == "success"){
                        window.location.reload()
                }
            },
            error: function(data){
                if (data.responseJSON.message !== null && data.responseJSON.message !== undefined && data.responseJSON.message !== '') {
                    alert(data.responseJSON.message);
                }else{
                    alert("新增失败");
                }
            }
        })
    }
}

//初始化基本信息窗口
function init_schedule_basic(){
    $("#pms_module_name_modal").val("0");
    $("#product_name_modal").val("0");
    $("#new_version").val("");
    $("#new_erp").select2("val", "0");
    $("#new_tqd").select2("val", "0");
    $("#new_manager").val("");
    $("#new_tester").val("");
    $("#new_test_commit_time").val("");
    $("#new_release_time").val("");
}

//初始化基本信息窗口
function init_schedule_detail(){
    $("#api_doc_time").val("");
    $("#api_mdf_num").val("");
    $("#case_num").val("");
    $("#p1_case_num").val("");
    $("#api_per_commit").val("");
    $("#case_per_commit").val("");
    $("#p1_case_num_f").val("");
    $("#case_num_f").val("");
    $("#desc").val("");
}

//修改基本信息
function edit_schedule_basic(r){
    $("#add_schedule_modal").attr("_e_init", "true");
    init_schedule_basic();
    var tr = $(r).parent("td").parent("tr");
    //$("#new_component").find('option:contains(' + $(tr).children()[1].innerHTML + ')').attr("selected", true);
    var pms_module_name = $(tr).children().eq(1).attr("_pms_module_name");
    var product_id = $(tr).children().eq(1).attr("_product_id");
    $("#pms_module_name_modal").val(pms_module_name);
    change_product_name(pms_module_name,product_id);
    //$("#product_name_modal").find('option:contains(' + product_name + ')').attr("selected", true);
    //$.ajax({
    //    type: 'GET',
    //    url : '/get_101_component/',
    //    dataType : 'json',
    //    success : function(data){
    //        //初始化下拉菜单
    //        $("#new_component").find("option").remove();
    //        $("#new_component").append('<option value="0">请选择</option>');
    //        for(var i=0;i<data.component_list.length;i++){
    //            var option = '<option value="' + data.component_list[i].id + '">' + data.component_list[i].component_name + '</option>';
    //            $("#new_component").append(option);
    //        }
    //成功后获取ERP数据
    $.ajax({
        type: 'GET',
        url : '/get_erp_items/',
        dataType : 'json',
        success : function(data){
            $("#add_schedule_modal").attr("_e_init", "false");
            //初始化下拉菜单
            $("#new_erp").find("option").remove();
            $("#new_erp").append('<option value="0">请选择</option>');
            for(var i=0;i<data.erp_list.length;i++){
                var option = '<option value="' + data.erp_list[i].code + '">' + data.erp_list[i].name + '</option>';
                $("#new_erp").append(option);
            }
            var tr = $(r).parent("td").parent("tr");
            var schedule_id = $(tr).children().eq(0).attr("id");
        //    $("#new_component").val($(tr).children()[1].innerHTML);
        //    $("#new_component").find('option:contains(' + $(tr).children()[1].innerHTML + ')').attr("selected", true);
            $("#new_version").val($(tr).children()[2].innerHTML);
            if($(tr).children().eq(3).attr("_erp_code") ==""){
                $("#new_erp").select2("val", "0");
                $("#new_tqd").select2("val", "0");
//                        $('#add_schedule_modal').modal('show');
            }
            else{
                $("#new_erp").select2("val", $(tr).children().eq(3).attr("_erp_code"));
                $.ajax({
                    type: 'GET',
                    url : '/get_tqd_list/?code=' + $(tr).children().eq(3).attr("_erp_code"),
                    dataType : 'json',
                    success : function(data){
                        //初始化下拉菜单
                        $("#new_tqd").find("option").remove();
                        $("#new_tqd").append('<option value="0">请选择</option>');
                        for(var i=0;i<data.tqd_list.items.length;i++){
                            var option = '<option value="' + data.tqd_list.items[i].id + '">' + "【" + data.tqd_list.items[i].id + "】" + data.tqd_list.items[i].title + '</option>';
                            $("#new_tqd").append(option);
                        }
                        $("#new_tqd").attr("disabled", false);
                        if($(tr).children()[3].innerHTML == ""){
                            $("#new_tqd").select2("val", "0");
                        }else{
                            $("#new_tqd").select2("val", $(tr).children()[3].innerHTML);
                        }
                    },
                    error: function(data){
                        $("#new_tqd").attr("disabled", false);
                        if (data.responseJSON.message !== null && data.responseJSON.message !== undefined && data.responseJSON.message !== '') {
                            alert(data.responseJSON.message);
                        }else{
                            alert("获取TQD列表失败");
                        }
                    }
                });
            }
            $("#new_manager").val($(tr).children()[4].innerHTML);
            $("#new_tester").val($(tr).children()[5].innerHTML);
            $("#new_test_commit_time").val($(tr).children()[6].innerHTML);
            $("#new_release_time").val($(tr).children()[7].innerHTML);
            var modal_footer = $("#edit_add_modal_footer");
            var button_close = $("<button type='button' class='btn btn-default' data-dismiss='modal'>关闭</button>");
            var button_save = $("<button type='button' onclick='edit_schedule_confirm(\"" + schedule_id + "\")' class='btn btn-primary'>保存</button>");
            $(modal_footer).empty()
                     .append(button_close)
                     .append(button_save);
            $('#add_schedule_modal').modal('show');
        },
        error: function(data){
            if (data.responseJSON.message !== null && data.responseJSON.message !== undefined && data.responseJSON.message !== '') {
                alert(data.responseJSON.message);
            }else{
                alert("获取ERP项目列表失败");
            }
        }
    })
    //    },
    //    error: function(data){
    //        if (data.responseJSON.message !== null && data.responseJSON.message !== undefined && data.responseJSON.message !== '') {
    //            alert(data.responseJSON.message);
    //        }else{
    //            alert("获取ERP项目列表失败");
    //        }
    //    }
    //});
}
function edit_schedule_confirm(schedule_id){
    if($("#pms_module_name_modal").val() == 0){
        alert_msg("请选择一级模块哦~");
    }else if($("#product_name_modal").val() == 0){
        alert_msg("请选择二级模块哦~");
    }else if($("#new_version").val() == ""){
        alert_msg("版本不能为空")
    }else if($("#new_manager").val() == ""){
        alert_msg("负责人不能为空")
    }else if($("#new_tester").val() == ""){
        alert_msg("测试人员不能为空")
    }else if($("#new_test_commit_time").val() == ""){
        alert_msg("提测时间不能为空")
    }else if($("#new_release_time").val() == ""){
        alert_msg("发布时间不能为空")
    }else{
        var postData = {
            "id": schedule_id,
            "component" : $("#product_name_modal").val(),
            "version" : $("#new_version").val(),
            "erp": $("#new_erp").val(),
            "tqd" : $("#new_tqd").val(),
            "manager" : $("#new_manager").val(),
            "tester" : $("#new_tester").val(),
            "test_commit_time" : $("#new_test_commit_time").val(),
            "release_time" : $("#new_release_time").val()
        };
        $.ajax({
            type: 'POST',
            url : '/schedule_edit/',
            data : postData,
            dataType : 'json',
            success : function(data){
                if(data.result == "fail"){
                    alert_msg("修改失败");
                }
                if(data.result == "success"){
                        window.location.reload()
                }
            },
            error: function(data){
                if (data.responseJSON.message !== null && data.responseJSON.message !== undefined && data.responseJSON.message !== '') {
                    alert(data.responseJSON.message);
                }else{
                    alert("修改失败");
                }
            }
        })
    }
}

function edit_schedule_detail(r){
    //初始化校验样式
    $("#edit_schedule_detail_modal div.control-group").removeClass("has-error");
    var tr = $(r).parent("td").parent("tr");
    var schedule_id = $(tr).children().eq(0).attr("id");
    init_schedule_detail();
    $.ajax({
        type: 'GET',
        url : '/get_schedule_detail?id=' + schedule_id,
        dataType : 'json',
        success : function(data){
            $("#api_doc_time").val(data.schedule_detail.api_doc_time);
            $("#api_mdf_num").val(data.schedule_detail.api_mdf_num);
            $("#case_num").val(data.schedule_detail.case_num);
            $("#p1_case_num").val(data.schedule_detail.p1_case_num);
            $("#api_per_commit").val(data.schedule_detail.api_per_commit);
            $("#case_per_commit").val(data.schedule_detail.case_per_commit);
            $("#p1_case_num_f").val(data.schedule_detail.p1_case_num_f);
            $("#case_num_f").val(data.schedule_detail.case_num_f);
            $("#desc").val(data.schedule_detail.desc);
        },
        error: function(data){
            if (data.responseJSON.message !== null && data.responseJSON.message !== undefined && data.responseJSON.message !== '') {
                alert(data.responseJSON.message);
            }else{
                alert("获取数据失败");
            }
        }
    });
    var modal_footer = $("#edit_schedule_detail_modal_footer");
    var button_close = $("<button type='button' class='btn btn-default' data-dismiss='modal'>关闭</button>");
    var button_save = $("<button type='button' onclick='edit_schedule_detail_confirm(\"" + schedule_id + "\")' class='btn btn-primary'>保存</button>");
    $(modal_footer).empty()
             .append(button_close)
             .append(button_save);
    $("#edit_schedule_detail_modal").modal("show");

}

function edit_schedule_detail_confirm(schedule_id){
    //初始化校验样式
    $("#edit_schedule_detail_modal div.control-group").removeClass("has-error");
    var error = "";
    $("#edit_schedule_detail_modal div.control-group").each(function(index,element){
        if(!check_key_num($(this).find("input").val())){
            $(this).addClass("has-error");
            error += $(this).prev().text().replace("：", "") + "，";
        }
    });
    if(error==""){
        var api_mdf_num = $("#api_mdf_num").val();
        var case_num = $("#case_num").val();
        var p1_case_num = $("#p1_case_num").val();
        var api_per_commit = $("#api_per_commit").val();
        var case_per_commit = $("#case_per_commit").val();
        var p1_case_num_f = $("#p1_case_num_f").val();
        var case_num_f = $("#case_num_f").val();
        if( parseInt(case_num)<parseInt(p1_case_num)){
            $("#p1_case_num").parent().parent().addClass("has-error");
            alert_msg("1级用例数大于用例总数");
        }
        if(parseInt(api_mdf_num)<parseInt(api_per_commit)){
            $("#api_per_commit").parent().parent().addClass("has-error");
            alert_msg("提测时覆盖的api数大于新增api数");
        }
        if(parseInt(case_num)<parseInt(case_per_commit)){
            $("#case_per_commit").parent().parent().addClass("has-error");
            alert_msg("提测时覆盖的用例数大于用例总数");
        }
//        if(case_num<p1_case_num_f){
//            $("#p1_case_num_f").parent().parent().addClass("has-error");
//            alert("1级用例覆盖数大于用例总数");
//        }
//        if(case_num<case_num_f){
//            $("#case_num_f").parent().parent().addClass("has-error");
//            alert("全用例覆盖数大于用例总数");
//        }
        if($("#edit_schedule_detail_modal div.has-error").length==0){
            var postData = {
                "id": schedule_id,
                "api_doc_time" : $("#api_doc_time").val(),
                "api_mdf_num" : $("#api_mdf_num").val(),
                "case_num": $("#case_num").val(),
                "p1_case_num" : $("#p1_case_num").val(),
                "api_per_commit" : $("#api_per_commit").val(),
                "case_per_commit" : $("#case_per_commit").val(),
                "p1_case_num_f" : $("#p1_case_num_f").val(),
                "case_num_f" : $("#case_num_f").val(),
                "desc" : $("#desc").val()
            };
            $.ajax({
                type: 'POST',
                url : '/edit_schedule_detail/',
                data : postData,
                dataType : 'json',
                success : function(data){
                    if(data.result == "fail"){
                        alert_msg("修改失败");
                    }
                    if(data.result == "success"){
                            window.location.reload()
                    }
                },
                error: function(data){
                    if (data.responseJSON.message !== null && data.responseJSON.message !== undefined && data.responseJSON.message !== '') {
                        alert(data.responseJSON.message);
                    }else{
                        alert("修改失败");
                    }
                }
            })
        }
    }else{
        alert_msg(error+"不是正整数");
    }
}

//搜索
function search(){
    var pms_module_name = $("#pms_module_name").val();
    var component_id = $("#product_name").val();
    var tqd = $("#tqd").val();
    var manager = $("#manager").val();
    $.ajax({
        type: 'GET',
        url : '/search_schedule/?pms_module_name='+pms_module_name+'&component_id=' + component_id + '&tqd=' + tqd+ '&manager=' + manager,
        dataType : 'json',
        success : function(data){
            $("#scheduleTable").remove();
            var schedule_list = data["schedule_list"];
            var table = "";
            table += "<table class=\"table table-bordered table-striped\" id=\"scheduleTable\">";
            table += "<thead>";
            table += "<tr>";
            table += '<th style="width:1%">编号</th>' +
                '<th style="width:8%">组件</th>' +
                '<th style="width:5%">版本</th>' +
                '<th style="width:5%">TQD</th>' +
                '<th style="width:5%">负责人</th>' +
                '<th style="width:5%">测试人员</th>' +
                '<th style="width:8%">提测时间</th>' +
                '<th style="width:8%">发布时间</th>' +
                '<th style="width:5%">操作</th>' +
                '<th style="width:8%">api文档提供时间</th>' +
                '<th style="width:5%">新增api数</th>' +
                '<th style="width:5%">提测时api覆盖率</th>' +
                '<th style="width:5%">提测时用例覆盖率</th>' +
                '<th style="width:5%">1级用例覆盖率</th>' +
                '<th style="width:5%">全用例覆盖率</th>' +
                '<th>备注</th>' +
                '<th style="width:10%">操作</th>';
            table += "</tr>";
            table += '</thead>';
            table += "<tbody id=\"table_body\">";
            for(var i=0;i<schedule_list.length;i++){
                var counter = i+1;
                table += '<tr>';
                table += '<td id="' + schedule_list[i].id + '">' + counter + '</td>' +
                    '<td _pms_module_name="' + schedule_list[i].pms_module_name + '" _product_id="' +
                        schedule_list[i].product_id + '">' + schedule_list[i].pms_module_name +":"+
                        schedule_list[i].product_name + '</td>' +
                    '<td>' + schedule_list[i].version + '</td>' +
                    '<td _erp_code="' + schedule_list[i].erp + '">' + schedule_list[i].tqd + '</td>' +
                    '<td>' + schedule_list[i].manager + '</td>' +
                    '<td>' + schedule_list[i].tester + '</td>' +
                    '<td>' + schedule_list[i].test_commit_time + '</td>' +
                    '<td>' + schedule_list[i].release_time + '</td>' +
                    '<td>' +
                    '<a class="btn btn-default" data-toggle="modal" onclick="edit_schedule_basic(this)" style="cursor:pointer">修改</a>' +
                    '</td>' +
                    '<td>' + schedule_list[i].api_doc_time + '</td>' +
                    '<td>' + schedule_list[i].api_mdf_num + '</td>' +
                    '<td>' + schedule_list[i].api_commit_per + '</td>' +
                    '<td>' + schedule_list[i].case_commit_per + '</td>' +
                    '<td>' + schedule_list[i].p1_case_per + '</td>' +
                    '<td>' + schedule_list[i].case_per + '</td>' +
                    '<td>' + schedule_list[i].desc + '</td>' +
                    '<td>' +
                    '<a class="btn btn-default" data-toggle="modal" onclick="edit_schedule_detail(this)" style="cursor:pointer">修改</a>&nbsp;&nbsp;' +
                    '<a class="btn btn-default" href="#modal-container-648300" data-toggle="modal" onclick="del_schedule(this)" style="cursor:pointer">删除</a>' +
                    '</td>';
            }
            table += "</tbody>";
            table += "</table>";
            $("#scheduleTableDiv").html(table);
            $('#scheduleTable').dataTable({
                "bPaginate": true,
                "bLengthChange": false,
                "iDisplayLength": 15,
                "bFilter": false,
                "bSort": true,
                "bInfo": true,
                "bAutoWidth": true,
                "oLanguage": {
                    "sEmptyTable":"无相关记录"
                },
                "pagingType": "full_numbers",
                "bDestroy":true,
                "retrieve": true
            });
        },
        error: function(data){
            if (data.responseJSON.message !== null && data.responseJSON.message !== undefined && data.responseJSON.message !== '') {
                alert(data.responseJSON.message);
            }else{
                alert("搜索失败");
            }
        }
    })

}

//删除版本进度
function del_schedule(r){
        var tr = $(r).parent("td").parent("tr");
        var index = $(tr).children().eq(0).attr("id");
        var button_close = $("<button type='button' class='btn btn-default' data-dismiss='modal'>关闭</button>");
        var button_save = $("<button type='button' onclick='delete_schedule_confirm(" + index + ")' class='btn btn-primary'>确定</button>");
        $("#delete_modal_footer").empty()
                .append(button_close)
                .append(button_save);
    }
function delete_schedule_confirm(index){
    var postData = {
            "schedule_id" : index
    };
    $.ajax({
        type: 'POST',
        url : '/del_schedule/',
        data : postData,
        dataType : 'json',
        success : function(data){
            if(data.result == "success"){
                window.location.reload()
            }
            else{
                alert("删除失败");
            }
        },
        error:function(data){
            if (data.responseJSON.message !== null && data.responseJSON.message !== undefined && data.responseJSON.message !== '') {
                alert(data.responseJSON.message);
            }else{
                alert("删除失败")
            }
        }
    })
}

//只能是数值验证
function check_key_num(a){
    var key_check = "^[0-9]*$";
    if(!a.match(key_check)){
        //不符合规则
        return false;
    }
    //符合规则
    return true;
}
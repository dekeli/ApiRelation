
//新增接口基本信息
function add_api_message() {
    var post_data = {};
    var myReg = /^[a-zA-Z0-9_~'!@#$%^&*()\-+=:;"/\\,.<>\{\}\[\]\s]{0,100}$/;
    post_data["component_owner"] = $("#api_component_input").val();
    post_data["request_name"] = $("#api_request_select").val();
    post_data["url_name"] = $("#api_url_input").val();
    post_data["name"] = $("#api_name_input").val();
    post_data["api_status"] = $("#api_status_select").val();
    if (post_data["component_owner"] == "" || post_data["url_name"] == ""){
         alert("请将必填信息填写完整");
         return;
    }
    else if(!myReg.test(post_data["component_owner"]) || !myReg.test(post_data["url_name"])){
        alert("接口服务或URL不可为中文");
        return;
    }
    $.ajax(
        {
            url: "/add_api/",
            type: "POST",
            dataType: "json",
            data: post_data,
            success:function(data) {
               if(data.result == "fail"){
                    alert("新增失败");
               }
               if(data.result == "success"){
                    alert("新增成功");
                    window.location.reload();
               }
               console.log(data)
            },
            error: function (data) {
                if(data.responseJSON.message !== null && data.responseJSON.message !== undefined && data.responseJSON.message !== '')
                {alert(data.responseJSON.message);}
                else {alert('新增失败');}
            }
        }
    )
};

//初始化基本信息窗口
function init_api_basic(x){
    var tr = $(x).parent("td").parent("tr");
    $("#edit_api_component_input").val($(tr).children().eq(1).attr("title"));
    $("#edit_api_request_select").val($(tr).children().eq(2).attr("title"));
    $("#edit_api_url_input").val($(tr).children().eq(3).attr("title"));
    $("#edit_api_name_input").val($(tr).children().eq(4).attr("title"));
    var status = $(tr).children().eq(5).text();
    var status2 = "";
    if(status == "在用"){status2 = "1";}
    else{status2="0"}
    $("#edit_api_status_select").val(status2);
}
//
//修改接口基本信息
function update_api_message(x) {
    init_api_basic(x);
    var put_data = {};
    var tr = $(x).parent("td").parent("tr");
    put_data["api_id"] = $(tr).children().eq(0).text();
    var myReg = /^[a-zA-Z0-9_~'!@#$%^&*()\-+=:;"/\\,.<>\{\}\[\]\s]{0,100}$/;
    put_data["edit_api_component"] = $("#edit_api_component_input").val();
    put_data["edit_api_request"] = $("#edit_api_request_select").val();
    put_data["edit_api_url"] = $("#edit_api_url_input").val();
    put_data["edit_api_name"] = $("#edit_api_name_input").val();
    put_data["edit_api_status"] = $("#edit_api_status_select").val();
    $("#edit_api_component_input").change(function(){
       put_data["edit_api_component"] = $("#edit_api_component_input").val();
    });
    $("#edit_api_request_select").change(function(){
       put_data["edit_api_request"] = $("#edit_api_request_select").val();
    });
    $("#edit_api_url_input").change(function(){
       put_data["edit_api_url"] = $("#edit_api_url_input").val();
    });
    $("#edit_api_name_input").change(function(){
       put_data["edit_api_name"] = $("#edit_api_name_input").val();
    });
    $("#edit_api_status_select").change(function(){
       put_data["edit_api_status"] = $("#edit_api_status_select").val();
    });
    $("#update_api_message_button").click(function(){
        if (put_data["component_owner"] == "" || put_data["url_name"] == ""){
             alert("请将必填信息填写完整");
             return;
        }
        else if(!myReg.test(put_data["component_owner"]) || !myReg.test(put_data["url_name"])){
            alert("接口服务或URL不可为中文");
            return;
        }
        $.ajax(
        {
            url: "/update_api/",
            type: "POST",
            dataType: "json",
            data: put_data,
            success:function(data) {
               if(data.result == "fail"){
                    alert("修改失败");
               }
               if(data.result == "success"){
                    alert("修改成功");
                    window.location.reload();
               }
               console.log(data)
            },
            error: function (data) {
                if(data.responseJSON.message !== null && data.responseJSON.message !== undefined && data.responseJSON.message !== '')
                {alert(data.responseJSON.message);}
                else {alert('修改失败');}
            }
        })
    });
}

//接口库条件查询
//function search_api(){
//    var post_data = {};
//    post_data["component_owner"] = $("#search-api-component").val();
//    post_data["request_name"] = $("#search-api-request").val();
//    post_data["url_name"] = $("#search-api-url").val();
//    $.ajax(
//        {
//            url: "/search_api/",
//            type: "POST",
//            dataType: "json",
//            data: post_data,
//            success:function(data) {
//               if(data.result == "success"){
//                   var table = "";
//                   table += "<table class=\"table\" id=\"table-api-list\">";
//                   table += "<thead>";
//                   table += "<tr>";
//                   table += "<th style=\"width: 5%\">编号</th>";
//                   table += " <th style=\"width: 15%\">所属组件服务</th>";
//                   table += "<th style=\"width: 7%\">请求方式</th>";
//                   table += "<th style=\"width: 30%\">路由</th>";
//                   table += "<th style=\"width: 15%\">接口名称</th>";
//                   table += "<th style=\"width: 8%\">是否在用</th>";
//                   table += "<th style=\"width: 20%\">操作</th>";
//                   table += "</tr>";
//                   table += "</thead>";
//                   table += "<tbody id=\"table_body\">";
//                   for(api in data["apis"]){
//                       table += "<tr>";
//                       table += "<td style=\"width: 5%\" >" + api.id +"</td>";
//                       table += "<td style=\"width: 15%\" title=\"" + api.component_owner +"\">"+ api.component_owner +"</td>";
//                       table += "<td style=\"width: 7%\" title=\"" + api.request_name +"\">"+ api.request_name +"</td>";
//                       table += "<td style=\"width: 30%\" title=\"" + api.url_name +"\">"+ api.url_name +"</td>";
//                       table += "<td style=\"width: 15%\" title=\"" + api.name +"\">"+ api.name +"</td>";
//                       if(api.status == 1){
//                           table += "<td style=\"width: 8%\">在用</td>";
//                       }
//                       else{
//                          table += "<td style=\"width: 8%\" title=\">禁用</td>";
//                       }
//                       table += "<td style=\"width: 20%\">";
//                       table += "<a class=\"btn btn-primary\" data-toggle=\"modal\" href=\"#update-api-window\" onclick=\"update_api_message(this)\">修改</a>";
//                       table += "<a class=\"btn btn-primary\" data-toggle=\"modal\">变更通知</a>";
//                       table += "<a class=\"btn btn-primary\" data-toggle=\"modal\">引用查询</a>";
//                       table += "</td>";
//                       table += "</tr>";
//                   }
//                   table += "</tbody>";
                   //var div = "";
                   //pages = data["pages"]
                   //apis = data["apis"]
                   //div += "<div class=\"col-xs-6\" style=\"width:25%;margin-top: 30px;\">";
                   //div += "<span>";
                   //div += "共 " + pages.count +" 条记录 当前第 " + apis.number + " 页 共 " + pages.num_pages + " 页";
                   //div += "</span>";
                   //div += "</div >";
                   //div += "<ul class=\"pagination\" style=\"float: right\">";
                   //div += "<li>";
                   //div += "<a href=\"?page=";
                   //if(apis.has_previous){div += apis.previous_page_number;}
                   //else{div += apis.number;}
                   //div += "\" aria-label=\"Previous\"><span aria-hidden=\"true\">&laquo;</span></a>";
                   //div += "</li>";
                   //for(page in pages.page_range){
                   //    div += "<li>";
                   //    div += "<a href=\"?page="+ page +"\">"+ page +"</a>";
                   //    div += "<li>";
                   //}
                   //div += "<li>";
                   //div += "<a href=\"?page=";
                   //if(apis.has_next){div += apis.next_page_number;}
                   //else{div += apis.number;}
                   //div += "\" aria-label=\"Next\"><span aria-hidden=\"true\">&laquo;</span></a>";
                   //div += "</li>";
                   //div += "</ul>";
//               }
//               $("#api_table_div").html(table);
//               console.log(data)
//            },
//            error: function (data) {
//                if(data.responseJSON.message !== null && data.responseJSON.message !== undefined && data.responseJSON.message !== '')
//                {alert(data.responseJSON.message);}
//                else {alert('查询失败');}
//            }
//        }
//    )
//}
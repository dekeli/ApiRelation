//接口表单公共校验方法
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

//修改接口基本信息
function update_api_message(x) {
    init_api_basic(x);
    var put_data = {};
    var tr = $(x).parent("td").parent("tr");

    put_data["edit_api_component"] = $("#edit_api_component_input").val();
    put_data["edit_api_request"] = $("#edit_api_request_select").val();
    put_data["edit_api_url"] = $("#edit_api_url_input").val();
    put_data["edit_api_name"] = $("#edit_api_name_input").val();
    put_data["edit_api_status"] = $("#edit_api_status_select").val();
};
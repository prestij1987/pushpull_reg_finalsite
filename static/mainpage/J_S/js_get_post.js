
function get(){

fetch("/project_pushpull/pushpull/J_S/js_get_post.js", {data}).
then((response)=>{return 
    response.json();}).
then((data_json)=>{
    console.log(data_json);})
};

console.log(get);
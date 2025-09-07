function get(){

    fetch("/project_pushpull/pushpull/account/account_form.js", {data}).
    then((response)=>{return 
        response.json();}).
    then((data_json)=>{
        console.log(data_json);})
    };
    
    console.log(get);
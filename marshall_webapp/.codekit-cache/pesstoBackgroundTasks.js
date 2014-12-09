// ============  CODEKIT IMPORTS  =========== //
//@codekit-prepend "utils/pesstoBackgroundTasks_utils.js";

$(function() {
    if (document.URL.indexOf("/transients") > -1) {
        console.log('updating sidebar list counts');
        $.post("/marshall/actions/refresh_sidebar_list_counts?method=put")
    }
});

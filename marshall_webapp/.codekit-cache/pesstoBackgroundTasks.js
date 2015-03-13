// ============  CODEKIT IMPORTS  =========== //
//@codekit-prepend "utils/pesstoBackgroundTasks_utils.js";

$(function() {
    if (document.URL.indexOf("/marshall/") > -1) {
        console.log('running update_pessto_meta_workflow_list_counts.py');
        $.post("/marshall/scripts/python/update_pessto_meta_workflow_list_counts.py")
    }
});

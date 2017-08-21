// ============  CODEKIT IMPORTS  =========== //
//@codekit-prepend "utils/dryxAnchors_utils.js";
//@codekit-prepend "_multi_link_exploder.js"; 

// Initisation 
$(function() {
    $(document.body).on("click", "a.postInBackground", post_to_url_in_background);
    $("div.objectLinkExploder").on("click", "button:first", multi_link_exploder);

});

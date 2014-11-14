// markdownwiki_move_page_form.js
// ===============================
// Author: Dave Young
// Date created: July 10, 2014
// Summary: Make new options lists appear whenever option changed in previous selection

var _markdownwiki_move_page_form = (function() {

    // -------------- Instantiate Module Attributes ---------------- // 
    var thisForm = $("form[action*='change_parent_id_of_md_page']");
    var rootSelect = thisForm.find("select[branch=0]");
    var controlGroup = rootSelect.closest("div.control-group");
    var branch = undefined;
    var thisSelect = undefined;
    var sqlQuery = undefined;
    var sqlToJson = undefined;
    var textAlert = undefined;
    var parentName = undefined;
    var newOptions = undefined;
    var allBranches = undefined;
    var checkArray = new Array();
    var thisUrl = "";
    // xt-initialise-variable

    // listen for changes on selects in modal form
    thisForm.on("change", "select[branch]", function() {
        // console.log('change function triggered');

        // find branch number of select that changed
        branch = $(this).attr("branch");
        $(this).attr("name", "parentId");
        // console.log('this branch changed: ' + branch);

        // select parent name and page id for selected option
        parentId = $(this).find("option:selected").attr("value");
        parentName = $(this).find("option:selected").text();
        // console.log('pageId of selected: ' + parentId);

        // remove newer branches
        $("select[branch]").each(function(index) {
            if ($(this).attr("branch") > branch) {
                console.log('this branch > last. branch no: ' + $(this).attr("branch"));
                $(this).closest(".controls").fadeOut(200, function() {
                    $(this).remove();
                });
            }
        });

        //remove text alert
        $("p.textAlert").fadeOut(200, function() {
            $("p.textAlert").remove();
        });

        // select titles and values for new select option (if any)
        sqlQuery = "select distinct title, pageId from base_md_pages where pageId in (select * from (select distinct pageId from base_md_pages where parentPageId = " + parentId + ") as alais) order by pageId, revisionNumber desc;"
        sqlQuery = encodeURIComponent(sqlQuery);
        thisUrl = window.location.toString();
        var parts = thisUrl.split('/apollo/');
        if (parts.length > 1) {
            thisUrl = "/apollo/assets/scripts/dryxScripts/sql_to_json.py?sqlQuery="
        } else {
            thisUrl = "/assets/scripts/dryxScripts/sql_to_json.py?sqlQuery="
            console.log('window.location: ' + window.location);

        }
        sqlToJson = $.ajax({
            url: thisUrl + sqlQuery,
            success: function(results) {
                // alert if this is the last branch in tree (no children)
                if (results.length === 0) {
                    text = '<p class="textAlert text-center text-info"><em>`' + parentName + "`</em> has no sub-pages</p>";
                    thisForm.append(text);
                    $("p.textAlert").hide().fadeIn(200);
                    // append options for sub-branches of the selected branch
                } else {
                    // clone a control group to use as tmeplate
                    newOptions = rootSelect.closest(".control-group").clone();
                    newOptions.find(".control-label").remove();

                    // update branch count
                    thisSelect = newOptions.find("select[branch]");
                    thisSelect.html("");
                    thisSelect.attr("branch", branch + 1).hide().fadeIn(200);
                    thisSelect.attr("name", "unselected");
                    // add options from sql-json object
                    thisOption = '<option value="none">select a sub-page</option>';
                    thisSelect.append(thisOption);
                    checkArray = [];
                    $.each(results, function(i, item) {
                        if ($.inArray(results[i].pageId, checkArray) === -1) {
                            thisOption = '<option value="' + results[i].pageId + '">' + results[i].title + '</option>'
                            thisSelect.append(thisOption);
                            checkArray.push(results[i].pageId);
                            console.log('pageId: ' + results[i].pageId);
                        } else {
                            console.log('nope!: ' + results[i].pageId);
                        }
                    });
                    thisForm.append(newOptions);
                }
            }
        });
    });
})();

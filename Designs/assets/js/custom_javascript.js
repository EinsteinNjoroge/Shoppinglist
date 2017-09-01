$(document).ready(function () {

    // initialize jquery datatable on the shoppingList
    var shoppingListTable = $("#shoppingListTable").DataTable({
        "paging": false,
        "info": false,
        columns: [
            {title: "Priority"},
            {title: "When I go to the store, I'll buy.."},
            {title: "Action"}
        ]
    });

    // initialize jquery datatable on shoppingList items
    var shoppingListItemsTable = $("#shoppingListItemsTable").DataTable({
        "paging": false,
        "info": false,
        columns: [
            {title: "Item"}
        ]
    });

    // initialize click listener on edit button
    var editBtn = $(".edit-btn");
    editBtn.click(function () {
        var currentRow = $(this).parents("tr");

        // remove event listeners on this row
        $(this).parents("tr").find("[data-ref]").off();

        // get id for the parent row and parent table
        var currentRowID = $(this).parents("tr").attr("id");
        var currentTable = $(this).parents("table");
        var currentTableID = $(currentTable).attr("id");

        // get data values from this row
        var currentTableRow = $("#" + currentTableID).DataTable().row(currentRow);
        var values = currentTableRow.data();

        // define an editor for each datatable
        var editor = null;
        if (currentTableID === "shoppingListTable") {
            editor = [
                "<input type=\"hidden\" name=\"identifier\" value=\"" + currentRowID + "\" />",
                "<textarea name=\"title\">" + values[1] + "</textarea>",
                "<button class=\"btn btn-primary\">Save</button>"
            ];
        } else if (currentTableID === "shoppingListItemsTable") {
            editor = [
                "<input type=\"hidden\" name=\"identifier\" value=\"" + currentRowID + "\" />" +
                "<textarea name=\"title\">" + values[0] + "</textarea>",
                "<button class=\"btn btn-primary\">Save</button>"
            ];
        }

        // update the UI with the editors
        currentTableRow.data(editor).draw();
    });

    // initialize click listener on delete button
    var deleteBtn = $(".delete-btn");
    deleteBtn.click(function () {
        var referenceLink = $(this).attr("delete-ref");

        // PopUp a confirmation dialog
        $.confirm({
            title: "Remove!",
            content: "Do you really want to remove this!",
            buttons: {
                remove: {
                    btnClass: "btn-danger",
                    action: function () {
                        window.location.href = referenceLink
                    }
                },
                cancel: {
                    btnClass: "btn-blue",
                    action: function () {
                        // do nothing
                    }
                }
            }
        });
    });

    // initialize click listener on delete elements with attribute `data-ref`
    var referenceLink = $("[data-ref]");
    referenceLink.click(function () {

        // redirect to new url
        window.location.href = $(this).attr("data-ref");
    });

});

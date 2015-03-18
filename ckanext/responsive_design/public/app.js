jQuery(function($) {
  window.multiView = null;
  window.explorerDiv = $('.data-explorer-here');
  

  // create the demo dataset
  //var dataset = createDemoDataset();
  // now create the multiview
  // this is rather more elaborate than the minimum as we configure the
  // MultiView in various ways (see function below)
  //window.multiview = createMultiView(dataset);

  // last, we'll demonstrate binding to changes in the dataset
  // this will print out a summary of each change onto the page in the
  // changelog section
  dataset.records.bind('all', function(name, obj) {
    var $info = $('<div />');
    //$info.html(name + ': ' + JSON.stringify(obj.toJSON()));
    $('.changelog').append($info);
    $('.changelog').show();
  });
});
 var data_from_json = {
    records: [
      {"s":"1",
        "p":"1",
        "o":"1"},
        {"s":"2",
        "p":"3",
        "o":"2"},
        {"s":"3",
        "p":"4",
        "o":"9"},
        {"s":"4",
        "p":"7",
        "o":"27"},
        {"s":"5",
        "p":"16",
        "o":"71"},
        {"s":"6",
        "p":"32",
        "o":"213"},
        {"s":"7",
        "p":"64",
        "o":"639"},
        {"s":"8",
        "p":"128",
        "o":"1800"
        }
    ],
    // let's be really explicit about fields
    // Plus take opportunity to set date to be a date field and set some labels
    fields: [
      {id: 's', type: 'string'},
      {id: 'p', type: 'string'},
      {id: 'o', type: 'string'}
    ]
  };
// create standard demo dataset
function createDemoDataset() {
 
  var dataset = new recline.Model.Dataset(data_from_json);
  console.log(dataset)
  return dataset;
}

// make MultivView
//
// creation / initialization in a function so we can call it again and again
var createMultiView = function(dataset, state) {
  // remove existing multiview if present
  var reload = false;
  if (window.multiView) {
    window.multiView.remove();
    window.multiView = null;
    reload = true;
  }

  var $el = $('<div />');
  $el.appendTo(window.explorerDiv);

  // customize the subviews for the MultiView
  var views = [
    {
      id: 'grid',
      label: 'Grid',
      view: new recline.View.SlickGrid({
        model: dataset,
        state: {
          gridOptions: {
            editable: false,
            // Enable support for row add
            enabledAddRow: false,
            // Enable support for row delete
            enabledDelRow: false,
            // Enable support for row ReOrder 
            enableReOrderRow:false,
            autoEdit: true,
            enableCellNavigation: true
          },
          columnsEditor: [
            { column: 'date', editor: Slick.Editors.Date },
            { column: 'title', editor: Slick.Editors.Text }
          ]
        }
      })
    },
    {
      id: 'graph',
      label: 'Graph',
      view: new recline.View.Graph({
        model: dataset

      })
    },
    {
      id: 'map',
      label: 'Map',
      view: new recline.View.Map({
        model: dataset
      })
    }
  ];
  console.log('views: ')
  console.log(views)
  var multiView = new recline.View.MultiView({
    model: dataset,
    el: $el,
    state: state,
    views: views
  });
  console.log('multiView: ')
  console.log(multiView)
  return multiView;
}


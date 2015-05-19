  $.getScript("/jquery-ui.min.js", function(){
   console.log("jquery loaded...");
}).complete(function(){

 $.getScript("/jquery-ui.js", function(){
   console.log("UI script loaded...");
   $("#querybuilderdiv").show();

}).complete(function(){

 function contains(array, element){
      var result = false;
      for(var i=0; i < array.length; i++)
          if(array[i] == element)
              return true
      return false;
  }
  $(function() {
    var url = "/query?query=PREFIX+void%3A+%3Chttp%3A%2F%2Frdfs.org%2Fns%2Fvoid%23%3E+PREFIX+geo%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23%3E+PREFIX+foaf%3A+%3Chttp%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2F%3E+PREFIX+vann%3A+%3Chttp%3A%2F%2Fpurl.org%2Fvocab%2Fvann%2F%3E+PREFIX+teach%3A+%3Chttp%3A%2F%2Flinkedscience.org%2Fteach%2Fns%23%3E+PREFIX+dcterms%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E+PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E+PREFIX+dcat%3A+%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fdcat%23%3E+PREFIX+crsw%3A+%3Chttp%3A%2F%2Fcourseware.rkbexplorer.com%2Fontologies%2Fcourseware%23%3E+PREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E+PREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E+PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E+PREFIX+aiiso%3A+%3Chttp%3A%2F%2Fpurl.org%2Fvocab%2Faiiso%2Fschema%23%3E+PREFIX+univcat%3A+%3Chttp%3A%2F%2Fdata.upf.edu%2Fupf%2Fontologies%2Funiversidadcatalana%23%3E+PREFIX+skos%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E+PREFIX+vivo%3A+%3Chttp%3A%2F%2Fvivoweb.org%2Fontology%2Fcore%23%3E+PREFIX+sbench%3A+%3Chttp%3A%2F%2Fswat.cse.lehigh.edu%2Fonto%2Funiv-bench.owl%23%3E+PREFIX+sdmx-attribute%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fattribute%23%3E+PREFIX+sdmx-concept%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fconcept%23%3E+PREFIX+sdmx-code%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fcode%23%3E+PREFIX+disco%3A+%3Chttp%3A%2F%2Frdf-vocabulary.ddialliance.org%2Fdiscovery%23%3E+PREFIX+sdmx-dimension%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fdimension%23%3E+PREFIX+sdmx-measure%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fmeasure%23%3E+PREFIX+qb%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fcube%23%3E+PREFIX+sdmx%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%23%3ESELECT+%3Fx%0AWHERE+%7B%0A++%3Fx+%3Fp+%3Fy.%0A%7D&server=http%3A%2F%2Fedem.eea.sk%3A8890%2Fsparql&direct_link=1&type_response_query=json";
    var json_all = $.getJSON(url).complete(function(){
    var json = json_all.responseJSON
    var availableTags = []
    for(var i=0; i < json.results.bindings.length; i++){
            if(contains(availableTags, json.results.bindings[i].x.value) == false)
                availableTags.push(json.results.bindings[i].x.value)
    }
    
    try{
    $( "#predicates" ).autocomplete({
      source: availableTags
    });
  }catch(TypeError){
    console.log("SUPER MEGA ERROR!!!")
    //location.reload();
  }
  });});
function addPredicate(){
    $("#2nd").show();
    $("#3rd").show();
    var val = $("#predicates").val();
    var val2 = $("#object").val();
    $(function() {
      // base url...
      var count = 0;
      for(var i=0; i < val.length; i++){
          if(val[i]=='/'){
              count++;
          }
      }
      for(var i= 0; i < count; i++){
          val= val.replace('/',"%2F");
      }
      
      
    val= val.replace(':',"%3A");
    val = val.replace('#','%23');
    var url = "/query?query=PREFIX+void%3A+%3Chttp%3A%2F%2Frdfs.org%2Fns%2Fvoid%23%3E+PREFIX+geo%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23%3E+PREFIX+foaf%3A+%3Chttp%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2F%3E+PREFIX+vann%3A+%3Chttp%3A%2F%2Fpurl.org%2Fvocab%2Fvann%2F%3E+PREFIX+teach%3A+%3Chttp%3A%2F%2Flinkedscience.org%2Fteach%2Fns%23%3E+PREFIX+dcterms%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E+PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E+PREFIX+dcat%3A+%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fdcat%23%3E+PREFIX+crsw%3A+%3Chttp%3A%2F%2Fcourseware.rkbexplorer.com%2Fontologies%2Fcourseware%23%3E+PREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E+PREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E+PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E+PREFIX+aiiso%3A+%3Chttp%3A%2F%2Fpurl.org%2Fvocab%2Faiiso%2Fschema%23%3E+PREFIX+univcat%3A+%3Chttp%3A%2F%2Fdata.upf.edu%2Fupf%2Fontologies%2Funiversidadcatalana%23%3E+PREFIX+skos%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E+PREFIX+vivo%3A+%3Chttp%3A%2F%2Fvivoweb.org%2Fontology%2Fcore%23%3E+PREFIX+sbench%3A+%3Chttp%3A%2F%2Fswat.cse.lehigh.edu%2Fonto%2Funiv-bench.owl%23%3E+PREFIX+sdmx-attribute%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fattribute%23%3E+PREFIX+sdmx-concept%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fconcept%23%3E+PREFIX+sdmx-code%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fcode%23%3E+PREFIX+disco%3A+%3Chttp%3A%2F%2Frdf-vocabulary.ddialliance.org%2Fdiscovery%23%3E+PREFIX+sdmx-dimension%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fdimension%23%3E+PREFIX+sdmx-measure%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fmeasure%23%3E+PREFIX+qb%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fcube%23%3E+PREFIX+sdmx%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%23%3ESELECT+%3Fp%0AWHERE%7B%0A%3Fs+%3Fp+%3Fo+%0AFILTER+REGEX(str(%3Fs)%2C+'%5E"+val+"%24')%0A%7D%0A&server=http%3A%2F%2Fedem.eea.sk%3A8890%2Fsparql&direct_link=1&type_response_query=json";

    var json_all = $.getJSON(url).complete(function(){
    var json = json_all.responseJSON
    var availableTags = []
    for(var i=0; i < json.results.bindings.length; i++){

            if(contains(availableTags, json.results.bindings[i].p.value) == false)
                availableTags.push(json.results.bindings[i].p.value)
    }
    

    $( "#subject" ).autocomplete({
      source: availableTags
    });


  });});
  
}
function showObject(){
  $("#3rd").show();}


var level = 1;
function genQuery(){
        var namespaces = "PREFIX void: <http://rdfs.org/ns/void#> \nPREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> \nPREFIX foaf: <http://xmlns.com/foaf/0.1/> \nPREFIX vann: <http://purl.org/vocab/vann/> \nPREFIX teach: <http://linkedscience.org/teach/ns#> \nPREFIX dcterms: <http://purl.org/dc/terms/> \nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nPREFIX dcat: <http://www.w3.org/ns/dcat#> \nPREFIX crsw: <http://courseware.rkbexplorer.com/ontologies/courseware#> \nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \nPREFIX owl: <http://www.w3.org/2002/07/owl#> \nPREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nPREFIX aiiso: <http://purl.org/vocab/aiiso/schema#> \nPREFIX univcat: <http://data.upf.edu/upf/ontologies/universidadcatalana#> \nPREFIX skos: <http://www.w3.org/2004/02/skos/core#> \nPREFIX vivo: <http://vivoweb.org/ontology/core#> \nPREFIX sbench: <http://swat.cse.lehigh.edu/onto/univ-bench.owl#> \nPREFIX sdmx-attribute: <http://purl.org/linked-data/sdmx/2009/attribute#> \nPREFIX sdmx-concept: <http://purl.org/linked-data/sdmx/2009/concept#> \nPREFIX sdmx-code: <http://purl.org/linked-data/sdmx/2009/code#> \nPREFIX disco: <http://rdf-vocabulary.ddialliance.org/discovery#> \nPREFIX sdmx-dimension: <http://purl.org/linked-data/sdmx/2009/dimension#> \nPREFIX sdmx-measure: <http://purl.org/linked-data/sdmx/2009/measure#> \nPREFIX qb: <http://purl.org/linked-data/cube#> \nPREFIX sdmx: <http://purl.org/linked-data/sdmx#> \n\n"
        var items = new Array();
        var criterias = new Array();
        var clazz = new Array();
        var number = 0;
        var _sub;
        var _obj;
        
        var query = namespaces;
        var predicates = $("#predicates").val();
        var subject = $("#subject").val();

        var object = $("#object").val();
        if($("#3rd").css( "visibility", "hidden" ).is( ":hidden" )){
          object = "";
        }
        var limit = $("#limit").val();
        if(limit == "" || limit == null)
          limit = 20;

        if(predicates == ""){ //000
          query+= "SELECT *\n WHERE{\n?s ?p ?o \n } \nLIMIT "+limit+" \n";
        }else if(predicates != "" && subject == "" && object == ""){ //100
          query += "SELECT * \nWHERE{\n?s ?p ?o \nFILTER REGEX(str(?s), '^"+predicates+"$')\n}\nLIMIT "+limit+" \n";
        }else if(predicates!= "" && subject != "" && object == ""){ //110
          query += "SELECT * \nWHERE{\n?s ?p ?o \nFILTER REGEX(str(?s), '^"+predicates+"$')\nFILTER REGEX(str(?p), '^"+subject+"$')\n}\nLIMIT "+limit+" \n";
        }else if(predicates != "" && subject == "" && object != ""){ //101
          query += "SELECT * \nWHERE{\n?s ?p ?o \nFILTER REGEX(str(?s), '^"+predicates+"$')\nFILTER REGEX(str(?o), '^"+object+"$')\n}\nLIMIT "+limit+" \n";
        }else if(predicates != "" && subject != "" && object != ""){ //111
          query += "SELECT * \nWHERE{\n?s ?p ?o \nFILTER REGEX(str(?s), '^"+predicates+"$')\nFILTER REGEX(str(?p), '^"+subject+"$')\nFILTER REGEX(str(?o), '^"+object+"$')\n}\nLIMIT "+limit+" \n";
        }

        console.log(query);

        editor.setValue(query);
      }

});

});
function addPredicate(){
    $("#2nd").show();
    $("#object").val("");
    var val = $("#predicates").val();
    $(function() {
      // base url...
      var count = 0;
      for(var i=0; i < val.length; i++){
          if(val[i]=='/'){
              count++;
          }
      }
      for(var i= 0; i < count; i++){
          val= val.replace('/',"%2F");
      }
      
      
      val= val.replace(':',"%3A");
      val = val.replace('#','%23');
     var url = "/query?query=PREFIX+void%3A+%3Chttp%3A%2F%2Frdfs.org%2Fns%2Fvoid%23%3E+PREFIX+geo%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2003%2F01%2Fgeo%2Fwgs84_pos%23%3E+PREFIX+foaf%3A+%3Chttp%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2F%3E+PREFIX+vann%3A+%3Chttp%3A%2F%2Fpurl.org%2Fvocab%2Fvann%2F%3E+PREFIX+teach%3A+%3Chttp%3A%2F%2Flinkedscience.org%2Fteach%2Fns%23%3E+PREFIX+dcterms%3A+%3Chttp%3A%2F%2Fpurl.org%2Fdc%2Fterms%2F%3E+PREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E+PREFIX+dcat%3A+%3Chttp%3A%2F%2Fwww.w3.org%2Fns%2Fdcat%23%3E+PREFIX+crsw%3A+%3Chttp%3A%2F%2Fcourseware.rkbexplorer.com%2Fontologies%2Fcourseware%23%3E+PREFIX+xsd%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2001%2FXMLSchema%23%3E+PREFIX+owl%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2002%2F07%2Fowl%23%3E+PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E+PREFIX+aiiso%3A+%3Chttp%3A%2F%2Fpurl.org%2Fvocab%2Faiiso%2Fschema%23%3E+PREFIX+univcat%3A+%3Chttp%3A%2F%2Fdata.upf.edu%2Fupf%2Fontologies%2Funiversidadcatalana%23%3E+PREFIX+skos%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2004%2F02%2Fskos%2Fcore%23%3E+PREFIX+vivo%3A+%3Chttp%3A%2F%2Fvivoweb.org%2Fontology%2Fcore%23%3E+PREFIX+sbench%3A+%3Chttp%3A%2F%2Fswat.cse.lehigh.edu%2Fonto%2Funiv-bench.owl%23%3E+PREFIX+sdmx-attribute%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fattribute%23%3E+PREFIX+sdmx-concept%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fconcept%23%3E+PREFIX+sdmx-code%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fcode%23%3E+PREFIX+disco%3A+%3Chttp%3A%2F%2Frdf-vocabulary.ddialliance.org%2Fdiscovery%23%3E+PREFIX+sdmx-dimension%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fdimension%23%3E+PREFIX+sdmx-measure%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%2F2009%2Fmeasure%23%3E+PREFIX+qb%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fcube%23%3E+PREFIX+sdmx%3A+%3Chttp%3A%2F%2Fpurl.org%2Flinked-data%2Fsdmx%23%3EPREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0APREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+swrc%3A+%3Chttp%3A%2F%2Fswrc.ontoware.org%2Fontology%23%3E%0A%0ASELECT+%3Fp%0AWHERE%7B%0A%09%3Fx+%3Fp+%3Fy+filter+regex(%3Fx%2C%22%5e"+val+"%24%22)%0A%7D&server=http%3A%2F%2Fedem.eea.sk%3A8890%2Fsparql&direct_link=1&type_response_query=json";

      //console.log(val);
      //console.log(url);

    var json_all = $.getJSON(url).complete(function(){
    var json = json_all.responseJSON
    var availableTags = []
    for(var i=0; i < json.results.bindings.length; i++){

            if(contains(availableTags, json.results.bindings[i].p.value) == false)
                availableTags.push(json.results.bindings[i].p.value)
    }
    

    $( "#subject" ).autocomplete({
      source: availableTags
    });
  });});
}

function genQuery(){
        var namespaces = "PREFIX void: <http://rdfs.org/ns/void#> \nPREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> \nPREFIX foaf: <http://xmlns.com/foaf/0.1/> \nPREFIX vann: <http://purl.org/vocab/vann/> \nPREFIX teach: <http://linkedscience.org/teach/ns#> \nPREFIX dcterms: <http://purl.org/dc/terms/> \nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nPREFIX dcat: <http://www.w3.org/ns/dcat#> \nPREFIX crsw: <http://courseware.rkbexplorer.com/ontologies/courseware#> \nPREFIX xsd: <http://www.w3.org/2001/XMLSchema#> \nPREFIX owl: <http://www.w3.org/2002/07/owl#> \nPREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nPREFIX aiiso: <http://purl.org/vocab/aiiso/schema#> \nPREFIX univcat: <http://data.upf.edu/upf/ontologies/universidadcatalana#> \nPREFIX skos: <http://www.w3.org/2004/02/skos/core#> \nPREFIX vivo: <http://vivoweb.org/ontology/core#> \nPREFIX sbench: <http://swat.cse.lehigh.edu/onto/univ-bench.owl#> \nPREFIX sdmx-attribute: <http://purl.org/linked-data/sdmx/2009/attribute#> \nPREFIX sdmx-concept: <http://purl.org/linked-data/sdmx/2009/concept#> \nPREFIX sdmx-code: <http://purl.org/linked-data/sdmx/2009/code#> \nPREFIX disco: <http://rdf-vocabulary.ddialliance.org/discovery#> \nPREFIX sdmx-dimension: <http://purl.org/linked-data/sdmx/2009/dimension#> \nPREFIX sdmx-measure: <http://purl.org/linked-data/sdmx/2009/measure#> \nPREFIX qb: <http://purl.org/linked-data/cube#> \nPREFIX sdmx: <http://purl.org/linked-data/sdmx#> \n\n"
        //var namespaces = "\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n\nPREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n\nPREFIX swrc: <http://swrc.ontoware.org/ontology#>\n\n";
        var items = new Array();
        var criterias = new Array();
        var clazz = new Array();
        var number = 0;
        var _sub;
        var _obj;
        
        var query = namespaces;
        var predicates = $("#predicates").val();
        var subject = $("#subject").val();
        var object = $("#object").val();
        var limit = $("#limit").val();
        if(limit == "" || limit == null)
          limit = 20;

        if(predicates == ""){ //000
          query+= "SELECT *\n WHERE{\n?s ?p ?o \n } \nLIMIT "+limit+" \n";
        }else if(predicates != "" && subject == "" && object == ""){ //100
          query += "SELECT * \nWHERE{\n?s ?p ?o \nFILTER REGEX(str(?s), '^"+predicates+"$')\n}\nLIMIT "+limit+" \n";
        }else if(predicates!= "" && subject != "" && object == ""){ //110
          query += "SELECT * \nWHERE{\n?s ?p ?o \nFILTER REGEX(str(?s), '^"+predicates+"$')\nFILTER REGEX(str(?p), '^"+subject+"$')\n}\nLIMIT "+limit+" \n";
        }else if(predicates != "" && subject == "" && object != ""){ //101
          query += "SELECT * \nWHERE{\n?s ?p ?o \nFILTER REGEX(str(?s), '^"+predicates+"$')\nFILTER REGEX(str(?o), '^"+object+"$')\n}\nLIMIT "+limit+" \n";
        }else if(predicates != "" && subject != "" && object != ""){ //111
          query += "SELECT * \nWHERE{\n?s ?p ?o \nFILTER REGEX(str(?s), '^"+predicates+"$')\nFILTER REGEX(str(?p), '^"+subject+"$')\nFILTER REGEX(str(?o), '"+object+"')\n}\nLIMIT "+limit+" \n";
        }

        console.log(query);
        
        editor.setValue(query);
      }

(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[2],{"0207":function(e,i,t){"use strict";t("934f")},"26ea":function(e,i,t){"use strict";t.r(i);var a=function(){var e=this,i=e.$createElement,t=e._self._c||i;return t("q-page",{staticClass:"flex flex-center background-cirf"},[!0===e.loading?t("div",{staticClass:"text-center"},[t("q-card-section",{staticClass:"q-py-lg"},[t("q-spinner",{attrs:{color:"white",size:"3em",thickness:5}})],1)],1):e._e(),"default"===e.eventData.modello_form_evento||""===e.eventData.modello_form_evento?t("DefaultForm",{attrs:{eventData:e.eventData,slug:e.$route.params.evento}}):"con_attivita"===e.eventData.modello_form_evento?t("DefaultFormConAttivita",{attrs:{eventData:e.eventData,slug:e.$route.params.evento}}):e._e()],1)},o=[],n=function(){var e=this,i=e.$createElement,t=e._self._c||i;return t("q-card",{staticClass:"main-form shadow-12"},[t("q-card-section",{staticClass:"q-py-none q-px-lg"},[t("div",{staticClass:"text-h6 q-my-lg text-primary text-center"},[e._v("Modulo di iscrizione all'evento")]),t("div",{staticClass:"text-h4 q-my-lg text-primary text-center"},[e._v(e._s(e.eventData.titolo))]),t("div",{staticClass:"q-my-lg row q-col-gutter-md"},[t("p",{staticClass:"col-12 col-sm-9 prespaced"},[e._v(e._s(e.eventData.descrizione))]),t("p",{staticClass:"col-12 col-sm-3 text-center"},[e.eventData.link&&""!==e.eventData.link?t("q-btn",{attrs:{rounded:"",outline:"",color:"primary",label:e.eventData.testo_link,size:"md",type:"a",href:e.eventData.link}}):e._e()],1)]),t("q-separator",{staticClass:"q-my-md"}),t("q-form",{staticClass:"q-my-lg",on:{submit:e.onSubmit}},[t("div",{staticClass:"row q-col-gutter-md"},[t("q-input",{staticClass:"col-12 col-sm-6",attrs:{autocomplete:"fname",label:"Nome *",hint:"Inserisci il tuo nome","lazy-rules":"",rules:[function(e){return e&&e.length>0||"Per favore inserisci il tuo nome"}]},model:{value:e.nome,callback:function(i){e.nome=i},expression:"nome"}}),t("q-input",{staticClass:"col-12 col-sm-6",attrs:{name:"cognome",autocomplete:"lname",label:"Cognome *",hint:"Inserisci il tuo cognome","lazy-rules":"",rules:[function(e){return e&&e.length>0||"Per favore inserisci il tuo cognome"}]},model:{value:e.cognome,callback:function(i){e.cognome=i},expression:"cognome"}}),t("q-input",{staticClass:"col-12 col-sm-6",attrs:{autocomplete:"email",label:"Email *",hint:"Inserisci la tua email",type:"email","lazy-rules":"",rules:[function(e){return e&&e.length>9&&e.includes("@")&&e.includes(".")||"Per favore inserisci un'email valida"}]},model:{value:e.email,callback:function(i){e.email=i},expression:"email"}})],1),t("q-list",{staticClass:"row"},[t("q-item",{directives:[{name:"ripple",rawName:"v-ripple"}],staticClass:"col-12 q-mt-lg",attrs:{tag:"label"}},[t("q-item-section",{attrs:{avatar:"",top:""}},[t("q-checkbox",{model:{value:e.desidera_crediti,callback:function(i){e.desidera_crediti=i},expression:"desidera_crediti"}})],1),t("q-item-section",[t("q-item-label",[e._v("Richiesta crediti")]),t("q-item-label",{attrs:{caption:""}},[e._v("Desidero siano riconosciuti crediti dal mio Ordine professionale")])],1)],1)],1),!0===e.desidera_crediti?t("div",{staticClass:"row q-mt-sm q-mb-lg q-col-gutter-md"},[t("q-input",{staticClass:"col-12 col-sm-6",attrs:{autocomplete:"codice_fiscale",label:"Codice Fiscale *",hint:"Inserisci il tuo codice fiscale","lazy-rules":"",rules:[function(e){return e&&e.length>8||"Per favore inserisci il tuo codice fiscale"}]},model:{value:e.codice_fiscale,callback:function(i){e.codice_fiscale=i},expression:"codice_fiscale"}}),t("q-select",{staticClass:"col-12 col-sm-6",attrs:{options:e.ordini_professionali,label:"Ordine professionale *",hint:"Inserisci l'Ordine professionale di appartenenza"},model:{value:e.ordine_di_appartenenza,callback:function(i){e.ordine_di_appartenenza=i},expression:"ordine_di_appartenenza"}}),t("q-select",{staticClass:"col-12 col-sm-4",attrs:{autocomplete:"region",options:e.regioni,label:"Regione *",hint:"Inserisci la Regione che ospita la sede dell'Ordine di appartenenza"},model:{value:e.regione,callback:function(i){e.regione=i},expression:"regione"}}),t("q-input",{staticClass:"col-12 col-sm-3",attrs:{autocomplete:"province",label:"Provincia",hint:"Inserisci la provincia che ospita la sede dell'Ordine di appartenenza","lazy-rules":"",rules:[function(e){return e&&2==e.length||"Per favore inserisci la sigla della provincia (2 caratteri)"}]},model:{value:e.provincia,callback:function(i){e.provincia=i},expression:"provincia"}}),t("q-input",{staticClass:"col-12 col-sm-3",attrs:{autocomplete:"matricola_ordine",label:"Num. iscrizione all'ordine *",hint:"Inserisci la matricola di iscrizione all'ordine","lazy-rules":"",rules:[function(e){return e&&e.length>0||"Per favore inserisci la tua matricola di iscrizione all'ordine"}]},model:{value:e.matricola_ordine,callback:function(i){e.matricola_ordine=i},expression:"matricola_ordine"}})],1):e._e(),t("q-list",{staticClass:"row"},[t("q-item",{directives:[{name:"ripple",rawName:"v-ripple"}],staticClass:"col-12",attrs:{tag:"label"}},[t("q-item-section",{attrs:{avatar:"",top:""}},[t("q-checkbox",{model:{value:e.iscrizione_newsletter,callback:function(i){e.iscrizione_newsletter=i},expression:"iscrizione_newsletter"}})],1),t("q-item-section",[t("q-item-label",[e._v("Iscrizione alla newsletter")]),t("q-item-label",{attrs:{caption:""}},[e._v("\n              Desidero iscrivermi alla newsletter dell'evento.\n              "),t("br"),e._v("La newsletter vi manterrà aggiornati sulle attività pre- e post-evento\n            ")])],1)],1),t("q-item",{directives:[{name:"ripple",rawName:"v-ripple"}],staticClass:"col-12",attrs:{tag:"label"}},[t("q-item-section",{attrs:{avatar:"",top:""}},[t("q-checkbox",{model:{value:e.accettazione_privacy,callback:function(i){e.accettazione_privacy=i},expression:"accettazione_privacy"}})],1),t("q-item-section",[t("q-item-label",[e._v("Autorizzo il trattamento dei dati *")]),t("q-item-label",{attrs:{caption:""}},[e._v("Autorizzo il trattamento dei dati per l'espletamento delle attività di iscrizione e partecipazione al convegno")])],1)],1)],1),t("q-separator",{staticClass:"q-my-md"}),t("div",{staticClass:"row"},[t("p",{staticClass:"prespaced col-12"},[e._v(e._s(e.eventData.istruzioni_finali))])]),t("div",{staticClass:"text-right"},[t("q-btn",{staticClass:"q-ml-sm",attrs:{label:"Torna indietro",color:"primary",flat:""},on:{click:function(i){return e.$router.push("/")}}}),t("q-btn",{attrs:{label:"Completa registrazione",type:"submit",color:"primary",loading:e.loading,disabled:e.loading}})],1)],1)],1)],1)},s=[],r=(t("b0c0"),t("82dc")),l=["Abruzzo","Basilicata","Calabria","Campania","Emilia-Romagna","Friuli-Venezia Giulia","Lazio","Liguria","Lombardia","Marche","Molise","Piemonte","Puglia","Sardegna","Sicilia","Toscana","Trentino-Alto Adige","Umbria","Valle d'Aosta","Veneto"],c=["Consiglio nazionale ingegneri","Consiglio nazionale architetti, pianificatori, paesaggisti e conservatori","Consiglio nazionale dei chimici","Consiglio nazionale dei geologi","Ordine nazionale dei biologi","Ordine nazionale dei dottori agronomi e dottori forestali"],d={name:"DefaultForm",props:["eventData","slug"],data:function(){return{nome:"",cognome:"",email:"",iscrizione_newsletter:!1,accettazione_privacy:!1,desidera_crediti:!1,codice_fiscale:"",matricola_ordine:"",regione:"",provincia:"",ordine_di_appartenenza:"",regioni:l,ordini_professionali:c,loading:!1}},methods:{onSubmit:function(){var e=this;if(!0!==this.accettazione_privacy)this.$q.notify({type:"negative",position:"top",message:"È necessario accettare l'autorizzazione al trattamento dei dati"});else try{this.loading=!0;var i="";this.$axios.get("https://eventi.cirf.org/csrf/").then((function(t){i=t.data.csrfToken,console.log(i),e.$axios.post("https://eventi.cirf.org/api/events/"+e.$route.params.evento+"/subscribe/",{nome:e.nome,cognome:e.cognome,email:e.email,iscrizione_newsletter:e.iscrizione_newsletter,accettazione_privacy:e.accettazione_privacy,desidera_crediti:e.desidera_crediti,codice_fiscale:e.codice_fiscale,matricola_ordine:e.matricola_ordine,regione:e.regione,provincia:e.provincia,ordine_di_appartenenza:e.ordine_di_appartenenza,csrfmiddlewaretoken:i},{headers:{"X-CSRFToken":i}}).then((function(i){var t=i.data;console.log(t),e.loading=!1,e.$q.notify({type:"positive",position:"top",message:"Registrazione avvenuta con successo"}),e.$router.push("/")})).catch((function(i){e.loading=!1,r["c"](i);var t="";t=i.response?500==i.response.status?"C'è un errore sul server, abbiamo avvisato il nostro staff. Siete pregati di riprovare più tardi":i.response.data.error+"  ("+i.response.status+")":i.request?"nessuna risposta ricevuta dal server":i.message,e.$q.notify({type:"negative",position:"top",timeout:0,actions:[{label:"CHIUDI",color:"white"}],caption:t,message:"Si è verificato un errore"})}))}))}catch(t){console.log(t),r["c"](t),this.loading=!1}},onReset:function(){this.name=null,this.age=null,this.accept=!1}}},m=d,p=(t("0207"),t("2877")),u=t("f09f"),v=t("a370"),g=t("9c40"),f=t("eb85"),_=t("0378"),b=t("27f9"),q=t("1c1c"),z=t("66e5"),h=t("4074"),C=t("8f8e"),y=t("0170"),x=t("ddd8"),k=t("714f"),w=t("eebe"),D=t.n(w),I=Object(p["a"])(m,n,s,!1,null,null,null),S=I.exports;D()(I,"components",{QCard:u["a"],QCardSection:v["a"],QBtn:g["a"],QSeparator:f["a"],QForm:_["a"],QInput:b["a"],QList:q["a"],QItem:z["a"],QItemSection:h["a"],QCheckbox:C["a"],QItemLabel:y["a"],QSelect:x["a"]}),D()(I,"directives",{Ripple:k["a"]});var Q=function(){var e=this,i=e.$createElement,t=e._self._c||i;return t("q-card",{staticClass:"main-form shadow-12"},[t("q-card-section",{staticClass:"q-py-none q-px-lg"},[t("div",{staticClass:"text-h6 q-my-lg text-primary text-center"},[e._v("Modulo di iscrizione all'evento")]),t("div",{staticClass:"text-h4 q-my-lg text-primary text-center"},[e._v(e._s(e.eventData.titolo))]),t("div",{staticClass:"q-my-lg row q-col-gutter-md"},[t("p",{staticClass:"col-12 col-sm-9 prespaced"},[e._v(e._s(e.eventData.descrizione))]),t("p",{staticClass:"col-12 col-sm-3 text-center"},[e.eventData.link&&""!==e.eventData.link?t("q-btn",{attrs:{rounded:"",outline:"",color:"primary",label:e.eventData.testo_link,size:"md",type:"a",href:e.eventData.link}}):e._e()],1)]),t("q-separator",{staticClass:"q-my-md"}),t("q-form",{staticClass:"q-my-lg",on:{submit:e.onSubmit}},[t("div",{staticClass:"row q-col-gutter-md"},[t("q-input",{staticClass:"col-12 col-sm-6",attrs:{autocomplete:"fname",label:"Nome *",hint:"Inserisci il tuo nome","lazy-rules":"",rules:[function(e){return e&&e.length>0||"Per favore inserisci il tuo nome"}]},model:{value:e.nome,callback:function(i){e.nome=i},expression:"nome"}}),t("q-input",{staticClass:"col-12 col-sm-6",attrs:{name:"cognome",autocomplete:"lname",label:"Cognome *",hint:"Inserisci il tuo cognome","lazy-rules":"",rules:[function(e){return e&&e.length>0||"Per favore inserisci il tuo cognome"}]},model:{value:e.cognome,callback:function(i){e.cognome=i},expression:"cognome"}}),t("q-input",{staticClass:"col-12 col-sm-6",attrs:{autocomplete:"email",label:"Email *",hint:"Inserisci la tua email",type:"email","lazy-rules":"",rules:[function(e){return e&&e.length>9&&e.includes("@")&&e.includes(".")||"Per favore inserisci un'email valida"}]},model:{value:e.email,callback:function(i){e.email=i},expression:"email"}})],1),t("div",{staticClass:"text-h6 q-my-lg text-primary"},[e._v("Attività a cui si desidera partecipare:")]),t("q-list",{staticClass:"row",staticStyle:{"background-color":"#EEE"}},e._l(e.eventData.attivita,(function(i){return t("q-item",{directives:[{name:"ripple",rawName:"v-ripple"}],key:i.pk,staticClass:"col-12",attrs:{tag:"label"}},[t("q-item-section",{attrs:{side:"",top:""}},[i.opzionale?t("q-checkbox",{model:{value:i.iscritto,callback:function(t){e.$set(i,"iscritto",t)},expression:"attivita.iscritto"}}):t("span",{staticStyle:{width:"40px"}},[e._v(" ")])],1),t("q-item-section",[t("q-item-label",{attrs:{overline:""}},[""!==i.inizio&&null!==i.inizio?t("span",[e._v(e._s(e.DateTime.fromISO(i.inizio).toLocaleString(e.DateTime.DATETIME_MED_WITH_WEEKDAY).toUpperCase()))]):e._e()]),t("q-item-label",[e._v(e._s(i.nome))]),t("q-item-label",{attrs:{caption:""}},[e._v(e._s(i.descrizione))])],1)],1)})),1),t("div",{staticClass:"text-h6 q-my-lg text-primary"},[e._v("Altre informazioni:")]),t("q-list",{staticClass:"row"},[t("q-item",{directives:[{name:"ripple",rawName:"v-ripple"}],staticClass:"col-12 q-mt-lg",attrs:{tag:"label"}},[t("q-item-section",{attrs:{avatar:"",top:""}},[t("q-checkbox",{model:{value:e.desidera_crediti,callback:function(i){e.desidera_crediti=i},expression:"desidera_crediti"}})],1),t("q-item-section",[t("q-item-label",[e._v("Richiesta crediti")]),t("q-item-label",{attrs:{caption:""}},[e._v("Desidero siano riconosciuti crediti dal mio Ordine professionale")])],1)],1)],1),!0===e.desidera_crediti?t("div",{staticClass:"row q-mt-sm q-mb-lg q-col-gutter-md"},[t("q-input",{staticClass:"col-12 col-sm-6",attrs:{autocomplete:"codice_fiscale",label:"Codice Fiscale *",hint:"Inserisci il tuo codice fiscale","lazy-rules":"",rules:[function(e){return e&&e.length>8||"Per favore inserisci il tuo codice fiscale"}]},model:{value:e.codice_fiscale,callback:function(i){e.codice_fiscale=i},expression:"codice_fiscale"}}),t("q-select",{staticClass:"col-12 col-sm-6",attrs:{options:e.ordini_professionali,label:"Ordine professionale *",hint:"Inserisci l'Ordine professionale di appartenenza"},model:{value:e.ordine_di_appartenenza,callback:function(i){e.ordine_di_appartenenza=i},expression:"ordine_di_appartenenza"}}),t("q-select",{staticClass:"col-12 col-sm-4",attrs:{autocomplete:"region",options:e.regioni,label:"Regione *",hint:"Inserisci la Regione che ospita la sede dell'Ordine di appartenenza"},model:{value:e.regione,callback:function(i){e.regione=i},expression:"regione"}}),t("q-input",{staticClass:"col-12 col-sm-3",attrs:{autocomplete:"province",label:"Provincia",hint:"Inserisci la provincia che ospita la sede dell'Ordine di appartenenza","lazy-rules":"",rules:[function(e){return e&&2==e.length||"Per favore inserisci la sigla della provincia (2 caratteri)"}]},model:{value:e.provincia,callback:function(i){e.provincia=i},expression:"provincia"}}),t("q-input",{staticClass:"col-12 col-sm-3",attrs:{autocomplete:"matricola_ordine",label:"Num. iscrizione all'ordine *",hint:"Inserisci la matricola di iscrizione all'ordine","lazy-rules":"",rules:[function(e){return e&&e.length>0||"Per favore inserisci la tua matricola di iscrizione all'ordine"}]},model:{value:e.matricola_ordine,callback:function(i){e.matricola_ordine=i},expression:"matricola_ordine"}})],1):e._e(),t("q-list",{staticClass:"row"},[t("q-item",{directives:[{name:"ripple",rawName:"v-ripple"}],staticClass:"col-12",attrs:{tag:"label"}},[t("q-item-section",{attrs:{avatar:"",top:""}},[t("q-checkbox",{model:{value:e.iscrizione_newsletter,callback:function(i){e.iscrizione_newsletter=i},expression:"iscrizione_newsletter"}})],1),t("q-item-section",[t("q-item-label",[e._v("Iscrizione alla newsletter")]),t("q-item-label",{attrs:{caption:""}},[e._v("\n              Desidero iscrivermi alla newsletter dell'evento.\n              "),t("br"),e._v("La newsletter vi manterrà aggiornati sulle attività pre- e post-evento\n            ")])],1)],1),t("q-item",{directives:[{name:"ripple",rawName:"v-ripple"}],staticClass:"col-12",attrs:{tag:"label"}},[t("q-item-section",{attrs:{avatar:"",top:""}},[t("q-checkbox",{model:{value:e.accettazione_privacy,callback:function(i){e.accettazione_privacy=i},expression:"accettazione_privacy"}})],1),t("q-item-section",[t("q-item-label",[e._v("Autorizzo il trattamento dei dati *")]),t("q-item-label",{attrs:{caption:""}},[e._v("Autorizzo il trattamento dei dati per l'espletamento delle attività di iscrizione e partecipazione al convegno")])],1)],1)],1),t("q-separator",{staticClass:"q-my-md"}),t("div",{staticClass:"row"},[t("p",{staticClass:"prespaced col-12"},[e._v(e._s(e.eventData.istruzioni_finali))])]),t("div",{staticClass:"text-right"},[t("q-btn",{staticClass:"q-ml-sm",attrs:{label:"Torna indietro",color:"primary",flat:""},on:{click:function(i){return e.$router.push("/")}}}),t("q-btn",{attrs:{label:"Completa registrazione",type:"submit",color:"primary",loading:e.loading,disabled:e.loading}})],1)],1)],1)],1)},$=[],A=(t("4de4"),t("d81d"),t("1315")),P=A.DateTime,O=["Abruzzo","Basilicata","Calabria","Campania","Emilia-Romagna","Friuli-Venezia Giulia","Lazio","Liguria","Lombardia","Marche","Molise","Piemonte","Puglia","Sardegna","Sicilia","Toscana","Trentino-Alto Adige","Umbria","Valle d'Aosta","Veneto"],T=["Consiglio nazionale ingegneri","Consiglio nazionale architetti, pianificatori, paesaggisti e conservatori","Consiglio nazionale dei chimici","Consiglio nazionale dei geologi","Ordine nazionale dei biologi","Ordine nazionale dei dottori agronomi e dottori forestali"],R={name:"DefaultFormConAttivita",props:["eventData","slug"],data:function(){return{nome:"",cognome:"",email:"",iscrizione_newsletter:!1,accettazione_privacy:!1,desidera_crediti:!1,codice_fiscale:"",matricola_ordine:"",regione:"",provincia:"",ordine_di_appartenenza:"",regioni:O,ordini_professionali:T,iscrizione_attivita:[],loading:!1,DateTime:P}},methods:{onSubmit:function(){var e=this;if(!0!==this.accettazione_privacy)this.$q.notify({type:"negative",position:"top",message:"È necessario accettare l'autorizzazione al trattamento dei dati"});else try{this.loading=!0;var i="";this.$axios.get("https://eventi.cirf.org/csrf/").then((function(t){i=t.data.csrfToken;var a=e.eventData.attivita.filter((function(e){return e.iscritto})).map((function(e){return e.pk}));console.log(i),e.$axios.post("https://eventi.cirf.org/api/events/"+e.$route.params.evento+"/subscribe/",{nome:e.nome,cognome:e.cognome,email:e.email,iscrizione_newsletter:e.iscrizione_newsletter,accettazione_privacy:e.accettazione_privacy,desidera_crediti:e.desidera_crediti,codice_fiscale:e.codice_fiscale,matricola_ordine:e.matricola_ordine,regione:e.regione,provincia:e.provincia,ordine_di_appartenenza:e.ordine_di_appartenenza,csrfmiddlewaretoken:i,attivita:a},{headers:{"X-CSRFToken":i}}).then((function(i){var t=i.data;console.log(t),e.loading=!1,e.$q.notify({type:"positive",position:"top",message:"Registrazione avvenuta con successo"}),e.$router.push("/")})).catch((function(i){e.loading=!1,r["c"](i);var t="";t=i.response?500==i.response.status?"C'è un errore sul server, abbiamo avvisato il nostro staff. Siete pregati di riprovare più tardi":i.response.data.error+"  ("+i.response.status+")":i.request?"nessuna risposta ricevuta dal server":i.message,e.$q.notify({type:"negative",position:"top",timeout:0,actions:[{label:"CHIUDI",color:"white"}],caption:t,message:"Si è verificato un errore"})}))}))}catch(t){console.log(t),r["c"](t),this.loading=!1}},onReset:function(){this.name=null,this.age=null,this.accept=!1}}},E=R,F=(t("728d"),Object(p["a"])(E,Q,$,!1,null,null,null)),L=F.exports;D()(F,"components",{QCard:u["a"],QCardSection:v["a"],QBtn:g["a"],QSeparator:f["a"],QForm:_["a"],QInput:b["a"],QList:q["a"],QItem:z["a"],QItemSection:h["a"],QCheckbox:C["a"],QItemLabel:y["a"],QSelect:x["a"]}),D()(F,"directives",{Ripple:k["a"]});var N={name:"Iscrizione",components:{DefaultForm:S,DefaultFormConAttivita:L},data:function(){return{loading:!0,eventData:""}},mounted:function(){var e=this;this.$axios.get("https://eventi.cirf.org/api/events/"+this.$route.params.evento+"/").then((function(i){e.eventData=i.data.evento,console.log(e.eventData),e.loading=!1})).catch((function(i){console.error(i),e.loading=!1}))}},M=N,V=(t("3e0e"),t("9989")),U=t("0d59"),B=Object(p["a"])(M,a,o,!1,null,null,null);i["default"]=B.exports;D()(B,"components",{QPage:V["a"],QCardSection:v["a"],QSpinner:U["a"]})},"2aa4":function(e,i,t){},"3e0e":function(e,i,t){"use strict";t("70e8")},"70e8":function(e,i,t){},"728d":function(e,i,t){"use strict";t("2aa4")},"934f":function(e,i,t){}}]);
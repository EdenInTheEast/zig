(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["main"],{

/***/ "+r5B":
/*!***********************************!*\
  !*** ./src/app/html.directive.ts ***!
  \***********************************/
/*! exports provided: HtmlDirective */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "HtmlDirective", function() { return HtmlDirective; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "fXoL");

class HtmlDirective {
    constructor(el) {
        el.nativeElement.style.backgroundColor = 'yellow';
    }
}
HtmlDirective.ɵfac = function HtmlDirective_Factory(t) { return new (t || HtmlDirective)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_0__["ElementRef"])); };
HtmlDirective.ɵdir = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineDirective"]({ type: HtmlDirective, selectors: [["", "appHtml", ""]] });


/***/ }),

/***/ 0:
/*!***************************!*\
  !*** multi ./src/main.ts ***!
  \***************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__(/*! /Users/rxgan/zig/angular/zig/src/main.ts */"zUnb");


/***/ }),

/***/ "1rY+":
/*!*************************************!*\
  !*** ./src/app/html/html.module.ts ***!
  \*************************************/
/*! exports provided: HtmlModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "HtmlModule", function() { return HtmlModule; });
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/common */ "ofXK");
/* harmony import */ var _div_div_component__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./div/div.component */ "DzY3");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/core */ "fXoL");



class HtmlModule {
}
HtmlModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineNgModule"]({ type: HtmlModule });
HtmlModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineInjector"]({ factory: function HtmlModule_Factory(t) { return new (t || HtmlModule)(); }, imports: [[
            _angular_common__WEBPACK_IMPORTED_MODULE_0__["CommonModule"]
        ]] });
(function () { (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵsetNgModuleScope"](HtmlModule, { declarations: [_div_div_component__WEBPACK_IMPORTED_MODULE_1__["DivComponent"]], imports: [_angular_common__WEBPACK_IMPORTED_MODULE_0__["CommonModule"]] }); })();


/***/ }),

/***/ "2aOy":
/*!*********************************************!*\
  !*** ./src/app/interfaces/component-map.ts ***!
  \*********************************************/
/*! exports provided: componentMap */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "componentMap", function() { return componentMap; });
/* harmony import */ var _main_graph_graph_component__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @main/graph/graph.component */ "V9mR");
/* harmony import */ var _html_div_div_component__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @html/div/div.component */ "DzY3");
// need better way to import all


const componentMap = {
    graph: _main_graph_graph_component__WEBPACK_IMPORTED_MODULE_0__["GraphComponent"],
    div: _html_div_div_component__WEBPACK_IMPORTED_MODULE_1__["DivComponent"],
};


/***/ }),

/***/ "2yus":
/*!*********************************!*\
  !*** ./src/app/rest.service.ts ***!
  \*********************************/
/*! exports provided: RestService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "RestService", function() { return RestService; });
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/common/http */ "tk/3");
/* harmony import */ var rxjs_operators__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! rxjs/operators */ "kU1M");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/core */ "fXoL");




class RestService {
    constructor(httpClient) {
        this.httpClient = httpClient;
        this.httpOptions = {
            headers: new _angular_common_http__WEBPACK_IMPORTED_MODULE_0__["HttpHeaders"]({ 'Content-Type': 'application/json' })
        };
    }
    getJSON(apiPoint, queryDict) {
        //need to add error handler	  	
        return this.httpClient.get(apiPoint, { params: queryDict ? queryDict : null }).pipe(Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_1__["retry"])(3));
    }
    putJSON(apiPoint, data) {
        //need to add error handler	  	
        this.response$ = this.httpClient.put(apiPoint, data, this.httpOptions).pipe(Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_1__["retry"])(3));
        return this.response$;
    }
    postJSON(apiPoint, data) {
        //need to add error handler	  	
        this.response$ = this.httpClient.post(apiPoint, data, this.httpOptions).pipe(Object(rxjs_operators__WEBPACK_IMPORTED_MODULE_1__["retry"])(3));
        return this.response$;
    }
}
RestService.ɵfac = function RestService_Factory(t) { return new (t || RestService)(_angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵinject"](_angular_common_http__WEBPACK_IMPORTED_MODULE_0__["HttpClient"])); };
RestService.ɵprov = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineInjectable"]({ token: RestService, factory: RestService.ɵfac, providedIn: 'root' });


/***/ }),

/***/ "AytR":
/*!*****************************************!*\
  !*** ./src/environments/environment.ts ***!
  \*****************************************/
/*! exports provided: environment */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "environment", function() { return environment; });
// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.
const environment = {
    production: false
};
/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.


/***/ }),

/***/ "DzY3":
/*!*******************************************!*\
  !*** ./src/app/html/div/div.component.ts ***!
  \*******************************************/
/*! exports provided: DivComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "DivComponent", function() { return DivComponent; });
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/common */ "ofXK");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "fXoL");


function DivComponent_ng_template_0_Template(rf, ctx) { }
class DivComponent {
    constructor(elementRef, renderer, document) {
        this.elementRef = elementRef;
        this.renderer = renderer;
        this.document = document;
        this.child = document.createElement('div');
    }
    ngOnInit() {
        this.createDom();
    }
    createDom() {
        // test function	  
        this.child.innerHTML = "test me";
        this.child.setAttribute("id", "Baby");
        const button = document.createElement('button');
        button.innerHTML = "click me";
        button.addEventListener("click", this.change);
        this.renderer.appendChild(this.elementRef.nativeElement, this.child);
        this.renderer.appendChild(this.elementRef.nativeElement, button);
    }
    change() {
        document.getElementById("Baby").innerHTML = "change!";
    }
    subscribeIn() {
    }
    subscribeOut() {
    }
}
DivComponent.ɵfac = function DivComponent_Factory(t) { return new (t || DivComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_1__["ElementRef"]), _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_1__["Renderer2"]), _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdirectiveInject"](_angular_common__WEBPACK_IMPORTED_MODULE_0__["DOCUMENT"])); };
DivComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineComponent"]({ type: DivComponent, selectors: [["app-div"]], inputs: { properties: "properties" }, decls: 1, vars: 0, template: function DivComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵtemplate"](0, DivComponent_ng_template_0_Template, 0, 0, "ng-template");
    } }, styles: ["\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJkaXYuY29tcG9uZW50LnNhc3MifQ== */"] });


/***/ }),

/***/ "SXOv":
/*!************************************************!*\
  !*** ./src/app/component-generator.service.ts ***!
  \************************************************/
/*! exports provided: ComponentGeneratorService */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "ComponentGeneratorService", function() { return ComponentGeneratorService; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "fXoL");

class ComponentGeneratorService {
    constructor(componentFactoryResolver) {
        this.componentFactoryResolver = componentFactoryResolver;
    }
    generateComponent(componentName) {
        //let componentFactory = this.componentFactoryResolver.resolveComponentFactory(componentName);
    }
}
ComponentGeneratorService.ɵfac = function ComponentGeneratorService_Factory(t) { return new (t || ComponentGeneratorService)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵinject"](_angular_core__WEBPACK_IMPORTED_MODULE_0__["ComponentFactoryResolver"])); };
ComponentGeneratorService.ɵprov = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineInjectable"]({ token: ComponentGeneratorService, factory: ComponentGeneratorService.ɵfac, providedIn: 'root' });


/***/ }),

/***/ "Sy1n":
/*!**********************************!*\
  !*** ./src/app/app.component.ts ***!
  \**********************************/
/*! exports provided: AppComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppComponent", function() { return AppComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "fXoL");
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common */ "ofXK");
/* harmony import */ var _html_div_div_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @html/div/div.component */ "DzY3");
/* harmony import */ var _interfaces_component_map__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! @interfaces/component-map */ "2aOy");
/* harmony import */ var _app_rest_service__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! @app/rest.service */ "2yus");






const _c0 = ["zigTemplate"];
class AppComponent {
    constructor(restService, componentFactoryResolver, injector, elementRef, renderer, document) {
        this.restService = restService;
        this.componentFactoryResolver = componentFactoryResolver;
        this.injector = injector;
        this.elementRef = elementRef;
        this.renderer = renderer;
        this.document = document;
        this.title = 'zig';
    }
    ngOnInit() { }
    ngAfterViewInit() {
        this.initializeApp();
        //this.getInitialData();
    }
    initializeApp() {
        this.restService.getJSON(AppComponent.initialApiEndPoint).subscribe((data) => {
            // use renderer to make custom html element
            this.jsonData = data['sections'];
            this.interactionData = data['interactions'];
            this.renderDOM(this.jsonData);
            this.renderInteractions(this.interactionData);
        });
    }
    renderDOM(sectionData) {
        for (let x in sectionData) {
            let type = sectionData[x]['dom_type'];
            let properties = sectionData[x]['data'];
            if (type != 'graph') {
                let ele = this.renderer.createElement(type);
                //set attributes
                for (let a in properties) {
                    this.renderer.setAttribute(ele, a, properties[a]);
                    if (a == 'content') {
                        this.renderer.setAttribute(ele, 'innerHTML', properties[a]);
                        ele.innerHTML = properties[a];
                    }
                }
                this.renderer.appendChild(this.elementRef.nativeElement, ele);
                for (let c in sectionData[x]['child']) {
                    //TODO: need to keep doing this recursively
                    let type = sectionData[x]['child'][c]['dom_type'];
                    let prop = sectionData[x]['child'][c]['data'];
                    let child = this.renderer.createElement(type);
                    for (let a in prop) {
                        this.renderer.setAttribute(child, a, prop[a]);
                        if (a == 'content') {
                            this.renderer.setAttribute(child, 'innerHTML', prop[a]);
                            child.innerHTML = prop[a];
                        }
                    }
                    this.renderer.appendChild(ele, child);
                }
            }
        }
    }
    renderInteractions(interactionData) {
        for (let interact in interactionData) {
            let apiUrl = interactionData[interact]['api_point'];
            //NOTE: Map() will have issue with JSON.stringify
            var inputs = interactionData[interact]['input'];
            var inputMap = this.getInputMap(inputs);
            this.setEventListener(inputs, inputMap, apiUrl);
            for (let o in interactionData[interact]['output']) {
                //NOTE: AT THIS POINT, python backend is the one 
                //determining and recording the INPUT and OUPUT 
                //relationships
            }
        }
    }
    getInputMap(inputs) {
        var inputMap = {};
        for (const [indx, input] of Object.entries(inputs)) {
            const inputElement = document.getElementById(input['id']);
            const inputValue = inputElement.getAttribute(input['attribute']);
            // create input Map first
            // send all input values on each change
            inputMap[indx] = { id: input['id'], dom_type: input['dom_type'], attribute: input['attribute'], value: inputValue };
            // TODO: need to handle Graph Object too
        }
        return inputMap;
    }
    setEventListener(inputs, inputMap, apiUrl) {
        for (const [k, i] of Object.entries(inputs)) {
            let inputID = i['id'];
            let inputType = i['dom_type'];
            let inputAttribute = i['attribute'];
            let inputObject = document.getElementById(inputID);
            //TODO:
            // - Input types with valueX
            // - mouse and key events
            // - other types' attributes
            // - JS elements' properties
            if (inputType == 'input' && inputAttribute == "value") {
                // this is only for input types' values
                this.renderer.listen(inputObject, 'change', (event) => {
                    inputMap[k]["value"] = event.target.value;
                    //TODO: need error handler
                    this.restService
                        .putJSON(apiUrl, inputMap)
                        .subscribe((data) => {
                        // THIS WILL RETURN OUTPUT CHANGE DATA
                        for (let d in data) {
                            this.updateChange(d, data[d]['attribute'], data[d]['data'], data[d]['dom_type']);
                        }
                    });
                });
            }
        }
    }
    updateChange(id, attribute, value, dom_type) {
        let element = document.getElementById(id);
        // for content type and html attribute
        attribute == "content" ? element.innerHTML = value : element.setAttribute(attribute, value);
        // TODO: others
        // graph type
    }
    try() {
        this.v = new _html_div_div_component__WEBPACK_IMPORTED_MODULE_2__["DivComponent"](this.elementRef, this.renderer, this.document);
        //this.v.properties = properties;
    }
    getInitialData() {
        this.restService.getJSON(AppComponent.initialApiEndPoint).subscribe((data) => {
            // creates component instead of html element
            //  uses NgContainer
            this.jsonData = data['sections'];
            console.log(this.jsonData);
            for (let x in this.jsonData) {
                let type = this.jsonData[x]['dom_type'];
                let properties = this.jsonData[x]['data'];
                // get Factory for each component and use that to create the component
                this.factoryResolver = this.componentFactoryResolver.resolveComponentFactory(_interfaces_component_map__WEBPACK_IMPORTED_MODULE_3__["componentMap"][type]);
                this.component = this.factoryResolver.create(this.injector);
                //let ele = this.component.location;
                //this.renderer.setAttribute(ele, 'appHtml', '');
                this.zigTemplate.insert(this.component.hostView);
                // store all components in a hashmap
                // auto pass all properties regardless of type
                this.component.instance.properties = properties;
            }
        });
    }
    renderComponent() {
        let resolver = this.componentFactoryResolver.resolveComponentFactory(_interfaces_component_map__WEBPACK_IMPORTED_MODULE_3__["componentMap"]['graph']);
        let componentFactory = this.zigTemplate.createComponent(resolver);
    }
}
//STORE THIS SEPARATELY, need to be able to set and share externally with python
//url use to get layout data from python
AppComponent.initialApiEndPoint = 'http://127.0.0.1:5000/api';
AppComponent.ɵfac = function AppComponent_Factory(t) { return new (t || AppComponent)(_angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_app_rest_service__WEBPACK_IMPORTED_MODULE_4__["RestService"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_0__["ComponentFactoryResolver"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_0__["Injector"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_0__["ElementRef"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_core__WEBPACK_IMPORTED_MODULE_0__["Renderer2"]), _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdirectiveInject"](_angular_common__WEBPACK_IMPORTED_MODULE_1__["DOCUMENT"])); };
AppComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: AppComponent, selectors: [["app-root"]], viewQuery: function AppComponent_Query(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵviewQuery"](_c0, 1, _angular_core__WEBPACK_IMPORTED_MODULE_0__["ViewContainerRef"]);
    } if (rf & 2) {
        let _t;
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵqueryRefresh"](_t = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵloadQuery"]()) && (ctx.zigTemplate = _t.first);
    } }, decls: 2, vars: 0, consts: [["zigTemplate", ""]], template: function AppComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelementContainer"](0, null, 0);
    } }, styles: ["\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJhcHAuY29tcG9uZW50LnNhc3MifQ== */"] });


/***/ }),

/***/ "V9mR":
/*!***********************************************!*\
  !*** ./src/app/main/graph/graph.component.ts ***!
  \***********************************************/
/*! exports provided: GraphComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "GraphComponent", function() { return GraphComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "fXoL");

class GraphComponent {
    constructor() {
        this.max = 100000;
    }
    ngOnInit() {
        if (!this.graphId) {
            this.generateGraphId();
        }
    }
    ngAfterViewInit() {
        this.createGraph(this.properties['data'], this.properties['layout']);
    }
    // graphData should be an object literal
    createGraph(graphData, graphLayout) {
        Plotly.newPlot(this.graphId, graphData, graphLayout);
    }
    generateGraphId() {
        this.graphId = (Math.random() * this.max).toString();
    }
}
GraphComponent.ɵfac = function GraphComponent_Factory(t) { return new (t || GraphComponent)(); };
GraphComponent.ɵcmp = _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵdefineComponent"]({ type: GraphComponent, selectors: [["app-graph"]], inputs: { properties: "properties" }, decls: 1, vars: 1, consts: [[2, "height", "100%", 3, "id"]], template: function GraphComponent_Template(rf, ctx) { if (rf & 1) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵelement"](0, "div", 0);
    } if (rf & 2) {
        _angular_core__WEBPACK_IMPORTED_MODULE_0__["ɵɵpropertyInterpolate"]("id", ctx.graphId);
    } }, styles: ["\n/*# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IiIsImZpbGUiOiJncmFwaC5jb21wb25lbnQuc2FzcyJ9 */"] });


/***/ }),

/***/ "XpXM":
/*!*************************************!*\
  !*** ./src/app/main/main.module.ts ***!
  \*************************************/
/*! exports provided: MainModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "MainModule", function() { return MainModule; });
/* harmony import */ var _angular_common__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/common */ "ofXK");
/* harmony import */ var _graph_graph_component__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./graph/graph.component */ "V9mR");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @angular/core */ "fXoL");



class MainModule {
}
MainModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineNgModule"]({ type: MainModule });
MainModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵdefineInjector"]({ factory: function MainModule_Factory(t) { return new (t || MainModule)(); }, imports: [[
            _angular_common__WEBPACK_IMPORTED_MODULE_0__["CommonModule"]
        ]] });
(function () { (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_2__["ɵɵsetNgModuleScope"](MainModule, { declarations: [_graph_graph_component__WEBPACK_IMPORTED_MODULE_1__["GraphComponent"]], imports: [_angular_common__WEBPACK_IMPORTED_MODULE_0__["CommonModule"]], exports: [_graph_graph_component__WEBPACK_IMPORTED_MODULE_1__["GraphComponent"]] }); })();


/***/ }),

/***/ "ZAI4":
/*!*******************************!*\
  !*** ./src/app/app.module.ts ***!
  \*******************************/
/*! exports provided: AppModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppModule", function() { return AppModule; });
/* harmony import */ var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/platform-browser */ "jhN1");
/* harmony import */ var _angular_common_http__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/common/http */ "tk/3");
/* harmony import */ var _app_routing_module__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./app-routing.module */ "vY5A");
/* harmony import */ var _app_component__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./app.component */ "Sy1n");
/* harmony import */ var _html_directive__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./html.directive */ "+r5B");
/* harmony import */ var _main_main_module__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! ./main/main.module */ "XpXM");
/* harmony import */ var _html_html_module__WEBPACK_IMPORTED_MODULE_6__ = __webpack_require__(/*! ./html/html.module */ "1rY+");
/* harmony import */ var _rest_service__WEBPACK_IMPORTED_MODULE_7__ = __webpack_require__(/*! ./rest.service */ "2yus");
/* harmony import */ var _component_generator_service__WEBPACK_IMPORTED_MODULE_8__ = __webpack_require__(/*! ./component-generator.service */ "SXOv");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_9__ = __webpack_require__(/*! @angular/core */ "fXoL");










class AppModule {
}
AppModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_9__["ɵɵdefineNgModule"]({ type: AppModule, bootstrap: [_app_component__WEBPACK_IMPORTED_MODULE_3__["AppComponent"]] });
AppModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_9__["ɵɵdefineInjector"]({ factory: function AppModule_Factory(t) { return new (t || AppModule)(); }, providers: [_rest_service__WEBPACK_IMPORTED_MODULE_7__["RestService"], _component_generator_service__WEBPACK_IMPORTED_MODULE_8__["ComponentGeneratorService"]], imports: [[
            _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__["BrowserModule"],
            _app_routing_module__WEBPACK_IMPORTED_MODULE_2__["AppRoutingModule"],
            _angular_common_http__WEBPACK_IMPORTED_MODULE_1__["HttpClientModule"],
            _main_main_module__WEBPACK_IMPORTED_MODULE_5__["MainModule"],
            _html_html_module__WEBPACK_IMPORTED_MODULE_6__["HtmlModule"],
        ]] });
(function () { (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_9__["ɵɵsetNgModuleScope"](AppModule, { declarations: [_app_component__WEBPACK_IMPORTED_MODULE_3__["AppComponent"],
        _html_directive__WEBPACK_IMPORTED_MODULE_4__["HtmlDirective"]], imports: [_angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__["BrowserModule"],
        _app_routing_module__WEBPACK_IMPORTED_MODULE_2__["AppRoutingModule"],
        _angular_common_http__WEBPACK_IMPORTED_MODULE_1__["HttpClientModule"],
        _main_main_module__WEBPACK_IMPORTED_MODULE_5__["MainModule"],
        _html_html_module__WEBPACK_IMPORTED_MODULE_6__["HtmlModule"]] }); })();


/***/ }),

/***/ "vY5A":
/*!***************************************!*\
  !*** ./src/app/app-routing.module.ts ***!
  \***************************************/
/*! exports provided: AppRoutingModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppRoutingModule", function() { return AppRoutingModule; });
/* harmony import */ var _angular_router__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/router */ "tyNb");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "fXoL");



const routes = [];
class AppRoutingModule {
}
AppRoutingModule.ɵmod = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineNgModule"]({ type: AppRoutingModule });
AppRoutingModule.ɵinj = _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵdefineInjector"]({ factory: function AppRoutingModule_Factory(t) { return new (t || AppRoutingModule)(); }, imports: [[_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"].forRoot(routes)], _angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]] });
(function () { (typeof ngJitMode === "undefined" || ngJitMode) && _angular_core__WEBPACK_IMPORTED_MODULE_1__["ɵɵsetNgModuleScope"](AppRoutingModule, { imports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]], exports: [_angular_router__WEBPACK_IMPORTED_MODULE_0__["RouterModule"]] }); })();


/***/ }),

/***/ "zUnb":
/*!*********************!*\
  !*** ./src/main.ts ***!
  \*********************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/platform-browser */ "jhN1");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "fXoL");
/* harmony import */ var _app_app_module__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./app/app.module */ "ZAI4");
/* harmony import */ var _environments_environment__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./environments/environment */ "AytR");




if (_environments_environment__WEBPACK_IMPORTED_MODULE_3__["environment"].production) {
    Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["enableProdMode"])();
}
_angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__["platformBrowser"]().bootstrapModule(_app_app_module__WEBPACK_IMPORTED_MODULE_2__["AppModule"])
    .catch(err => console.error(err));


/***/ }),

/***/ "zn8P":
/*!******************************************************!*\
  !*** ./$$_lazy_route_resource lazy namespace object ***!
  \******************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

function webpackEmptyAsyncContext(req) {
	// Here Promise.resolve().then() is used instead of new Promise() to prevent
	// uncaught exception popping up in devtools
	return Promise.resolve().then(function() {
		var e = new Error("Cannot find module '" + req + "'");
		e.code = 'MODULE_NOT_FOUND';
		throw e;
	});
}
webpackEmptyAsyncContext.keys = function() { return []; };
webpackEmptyAsyncContext.resolve = webpackEmptyAsyncContext;
module.exports = webpackEmptyAsyncContext;
webpackEmptyAsyncContext.id = "zn8P";

/***/ })

},[[0,"runtime","vendor"]]]);
//# sourceMappingURL=main.js.map
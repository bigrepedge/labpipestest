(function (e) { function t (t) { for (var r, s, u = t[0], i = t[1], c = t[2], p = 0, v = []; p < u.length; p++)s = u[p], a[s] && v.push(a[s][0]), a[s] = 0; for (r in i)Object.prototype.hasOwnProperty.call(i, r) && (e[r] = i[r]); l && l(t); while (v.length)v.shift()(); return o.push.apply(o, c || []), n() } function n () { for (var e, t = 0; t < o.length; t++) { for (var n = o[t], r = !0, u = 1; u < n.length; u++) { var i = n[u]; a[i] !== 0 && (r = !1) }r && (o.splice(t--, 1), e = s(s.s = n[0])) } return e } var r = {}, a = {1: 0}, o = []; function s (t) { if (r[t]) return r[t].exports; var n = r[t] = {i: t, l: !1, exports: {}}; return e[t].call(n.exports, n, n.exports, s), n.l = !0, n.exports }s.m = e, s.c = r, s.d = function (e, t, n) { s.o(e, t) || Object.defineProperty(e, t, {enumerable: !0, get: n}) }, s.r = function (e) { typeof Symbol !== 'undefined' && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {value: 'Module'}), Object.defineProperty(e, '__esModule', {value: !0}) }, s.t = function (e, t) { if (1 & t && (e = s(e)), 8 & t) return e; if (4 & t && typeof e === 'object' && e && e.__esModule) return e; var n = Object.create(null); if (s.r(n), Object.defineProperty(n, 'default', {enumerable: !0, value: e}), 2 & t && typeof e !== 'string') for (var r in e)s.d(n, r, function (t) { return e[t] }.bind(null, r)); return n }, s.n = function (e) { var t = e && e.__esModule ? function () { return e['default'] } : function () { return e }; return s.d(t, 'a', t), t }, s.o = function (e, t) { return Object.prototype.hasOwnProperty.call(e, t) }, s.p = '/'; var u = window['webpackJsonp'] = window['webpackJsonp'] || [], i = u.push.bind(u); u.push = t, u = u.slice(); for (var c = 0; c < u.length; c++)t(u[c]); var l = i; o.push([3, 0]), n() })({3: function (e, t, n) { e.exports = n('Vtdi') }, EDI0: function (e, t, n) {}, Lh0y: function (e, t, n) { 'use strict'; var r = n('txWo'), a = n.n(r); a.a }, Vtdi: function (e, t, n) { 'use strict'; n.r(t); n('VRzm'); var r = n('Kw5r'), a = function () { var e = this, t = e.$createElement, n = e._self._c || t; return n('div', {attrs: {id: 'app'}}, [n('div', {attrs: {id: 'navbar'}}, [n('div', {staticClass: 'brand'}), n('div', {staticClass: 'main-menu'}, [n('router-link', {attrs: {to: '/devhelp'}}, [e._v('Dev Helpful Links')]), n('router-link', {attrs: {to: '/'}}, [e._v('Demo')])], 1)]), n('router-view')], 1) }, o = [], s = (n('ZL7j'), n('KHd+')), u = {}, i = Object(s['a'])(u, a, o, !1, null, null, null), c = i.exports, l = n('jE9Z'), p = function () { var e = this, t = e.$createElement, n = e._self._c || t; return n('div', {staticClass: 'content'}, [n('div', {staticClass: 'panel'}, [n('HelpLinks', {attrs: {msg: 'This is a list of some useful links'}})], 1)]) }, v = [], f = function () { var e = this, t = e.$createElement, n = e._self._c || t; return n('div', {staticClass: 'hello'}, [n('h1', [e._v(e._s(e.msg))]), e._m(0), n('h3', [e._v('Installed CLI Plugins')]), e._m(1), n('h3', [e._v('More Links')]), e._m(2), n('h3', [e._v('plugins')]), e._m(3), n('h3', [e._v('Testing plugins')]), e._m(4)]) }, h = [function () { var e = this, t = e.$createElement, n = e._self._c || t; return n('p', [e._v('\n    For guide about the vue software stack take a look here.\n    '), n('a', {attrs: {href: 'https://github.com/vuejs/vue-cli/tree/dev/docs', target: '_blank'}}, [e._v('vue-cli documentation')])]) }, function () { var e = this, t = e.$createElement, n = e._self._c || t; return n('ul', [n('li', [n('a', {attrs: {href: 'https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel', target: '_blank'}}, [e._v('babel')])]), n('li', [n('a', {attrs: {href: 'https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint', target: '_blank'}}, [e._v('eslint')])])]) }, function () { var e = this, t = e.$createElement, n = e._self._c || t; return n('ul', [n('li', [n('a', {attrs: {href: 'https://vuejs.org', target: '_blank'}}, [e._v('Vuejs')])])]) }, function () { var e = this, t = e.$createElement, n = e._self._c || t; return n('ul', [n('li', [n('a', {attrs: {href: 'https://router.vuejs.org/en/essentials/getting-started.html', target: '_blank'}}, [e._v('vue-router')])]), n('li', [n('a', {attrs: {href: 'https://vuex.vuejs.org/en/intro.html', target: '_blank'}}, [e._v('vuex')])]), n('li', [n('a', {attrs: {href: 'https://github.com/vuejs/vue-devtools#vue-devtools', target: '_blank'}}, [e._v('vue-devtools')])]), n('li', [n('a', {attrs: {href: 'https://vue-loader.vuejs.org/en', target: '_blank'}}, [e._v('vue-loader')])]), n('li', [n('a', {attrs: {href: 'https://github.com/vuejs/awesome-vue', target: '_blank'}}, [e._v('awesome-vue')])])]) }, function () { var e = this, t = e.$createElement, n = e._self._c || t; return n('ul', [n('li', [n('a', {attrs: {href: 'https://pytest-cov.readthedocs.io/en/latest/', target: '_blank'}}, [e._v('pytest')])]), n('li', [n('a', {attrs: {href: 'https://docs.cypress.io/guides/overview/why-cypress.html#', target: '_blank'}}, [e._v('cypress')])]), n('li', [n('a', {attrs: {href: 'https://facebook.github.io/jest/', target: '_blank'}}, [e._v('jest')])])]) }], m = {name: 'HelpLinks', props: {msg: String}}, _ = m, d = Object(s['a'])(_, f, h, !1, null, null, null), b = d.exports, g = {name: 'DevHelp', components: {HelpLinks: b}}, k = g, T = Object(s['a'])(k, p, v, !1, null, null, null), j = T.exports, y = function () { var e = this, t = e.$createElement, n = e._self._c || t; return n('div', {staticClass: 'content'}, [n('div', {staticClass: 'panel'}, [n('h1', [e._v('BigRep HMI Demo')]), e.notConnected ? n('button', {staticClass: 'btn', on: {click: e.connectToPrinter}}, [e._v('Connect to printer')]) : n('div', [n('h4', [e._v('Temperatures')]), e.elementTemperature ? n('p', [e._v(e._s(e._f('formatTemp')(e.elementTemperature)))]) : e._e(), n('button', {staticClass: 'btn', on: {click: function (t) { e.fetchTemperatureResource('Bed') }}}, [e._v('Bed')]), n('button', {staticClass: 'btn', on: {click: function (t) { e.fetchTemperatureResource('Extruder0') }}}, [e._v('T0')]), n('button', {staticClass: 'btn', on: {click: function (t) { e.fetchTemperatureResource('Extruder1') }}}, [e._v('T1')]), n('button', {staticClass: 'btn', on: {click: function (t) { e.fetchTemperatureResource('Chamber') }}}, [e._v('Chamber')])]), n('p', [e._v(e._s(e.error))])])]) }, w = [], C = n('vDqi'), x = n.n(C), E = !0, L = E ? '/api/' : 'http://localhost:5000/api/', O = x.a.create({baseURL: L, timeout: 5e3, headers: {'Content-Type': 'application/json'}}); O.interceptors.request.use(function (e) { return e.headers['Authorization'] = 'Fake Token', e }), O.interceptors.response.use(function (e) { return e }, function (e) { return Promise.reject(e) }); var P = {connectToPrinter: function () { return O.get('connect/user').then(function (e) { return e.data }) }, fetchTemperatureResource: function (e) { var t = 'temperature/' + e; return O.get(t).then(function (e) { return e.data }) }}, S = {name: 'api', data: function () { return {elementTemperature: void 0, error: '', notConnected: !0} }, methods: {connectToPrinter: function () { var e = this; P.connectToPrinter().then(function (t) { e.showGetTempButtons() }).catch(function (t) { e.error = t.message }) }, fetchTemperatureResource: function (e) { var t = this; P.fetchTemperatureResource(e).then(function (e) { t.elementTemperature = e }).catch(function (e) { t.error = e.message }) }, showGetTempButtons: function () { this.notConnected = !1 }}}, R = S, $ = (n('Lh0y'), Object(s['a'])(R, y, w, !1, null, '5dc929b9', null)), D = $.exports; r['a'].use(l['a']); var H = new l['a']({routes: [{path: '/', name: 'api', component: D}, {path: '/devhelp', name: 'devhelp', component: j}]}), I = n('L2JU'); r['a'].use(I['a']); var M = new I['a'].Store({state: {}, mutations: {}, actions: {}}), B = {formatTimes: function (e) { var t = new Date(e); return t.toLocaleTimeString('en-US') }, formatTimestamp: function (e) { var t = new Date(e); return t.toLocaleTimeString('en-US') }, formatTemp: function (e) { var t = e.heating_element.concat(': ', ' Target ', e.target_temp, ' Actual ', parseInt(e.actual_temp)); return t }}; Object.keys(B).forEach(function (e) { r['a'].filter(e, B[e]) }), r['a'].config.productionTip = !1, new r['a']({router: H, store: M, render: function (e) { return e(c) }}).$mount('#app') }, ZL7j: function (e, t, n) { 'use strict'; var r = n('EDI0'), a = n.n(r); a.a }, txWo: function (e, t, n) {}})
// # sourceMappingURL=app.61efda2f.js.map

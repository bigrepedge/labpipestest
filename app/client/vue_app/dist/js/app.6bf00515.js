(function (e) { function t (t) { for (var n, a, i = t[0], c = t[1], s = t[2], l = 0, p = []; l < i.length; l++)a = i[l], o[a] && p.push(o[a][0]), o[a] = 0; for (n in c)Object.prototype.hasOwnProperty.call(c, n) && (e[n] = c[n]); f && f(t); while (p.length)p.shift()(); return u.push.apply(u, s || []), r() } function r () { for (var e, t = 0; t < u.length; t++) { for (var r = u[t], n = !0, i = 1; i < r.length; i++) { var c = r[i]; o[c] !== 0 && (n = !1) }n && (u.splice(t--, 1), e = a(a.s = r[0])) } return e } var n = {}, o = {1: 0}, u = []; function a (t) { if (n[t]) return n[t].exports; var r = n[t] = {i: t, l: !1, exports: {}}; return e[t].call(r.exports, r, r.exports, a), r.l = !0, r.exports }a.m = e, a.c = n, a.d = function (e, t, r) { a.o(e, t) || Object.defineProperty(e, t, {enumerable: !0, get: r}) }, a.r = function (e) { typeof Symbol !== 'undefined' && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {value: 'Module'}), Object.defineProperty(e, '__esModule', {value: !0}) }, a.t = function (e, t) { if (1 & t && (e = a(e)), 8 & t) return e; if (4 & t && typeof e === 'object' && e && e.__esModule) return e; var r = Object.create(null); if (a.r(r), Object.defineProperty(r, 'default', {enumerable: !0, value: e}), 2 & t && typeof e !== 'string') for (var n in e)a.d(r, n, function (t) { return e[t] }.bind(null, n)); return r }, a.n = function (e) { var t = e && e.__esModule ? function () { return e['default'] } : function () { return e }; return a.d(t, 'a', t), t }, a.o = function (e, t) { return Object.prototype.hasOwnProperty.call(e, t) }, a.p = '/'; var i = window['webpackJsonp'] = window['webpackJsonp'] || [], c = i.push.bind(i); i.push = t, i = i.slice(); for (var s = 0; s < i.length; s++)t(i[s]); var f = c; u.push([1, 0]), r() })({1: function (e, t, r) { e.exports = r('Vtdi') }, Vtdi: function (e, t, r) { 'use strict'; r.r(t); var n = r('Kw5r'), o = function () { var e = this, t = e.$createElement, r = e._self._c || t; return r('div', {attrs: {id: 'app'}}, [e._m(0), r('router-view')], 1) }, u = [function () { var e = this, t = e.$createElement, r = e._self._c || t; return r('div', {attrs: {id: 'navbar'}}, [r('div', {staticClass: 'brand'}), r('div', {staticClass: 'main-menu'})]) }], a = (r('nNx0'), r('KHd+')), i = {}, c = Object(a['a'])(i, o, u, !1, null, null, null), s = c.exports, f = r('jE9Z'), l = function () { var e = this, t = e.$createElement, r = e._self._c || t; return r('div', {staticClass: 'content'}, [r('div', {staticClass: 'panel'}, [r('p', [e._v('Click on the links below to fetch data from the Flask server')]), r('p', [e._v('testing random stuff')]), r('a', {attrs: {href: ''}, on: {click: function (t) { return t.preventDefault(), e.fetchResource(t) }}}, [e._v('Fetch Resource')]), r('br'), r('h4', [e._v('Results')]), e._l(e.resources, function (t) { return r('p', {key: t.timestamp}, [e._v('\n      Server Timestamp: ' + e._s(e._f('formatTimestamp')(t.timestamp)) + '\n    ')]) }), r('p', [e._v(e._s(e.error))])], 2)]) }, p = [], v = (r('VRzm'), r('vDqi')), h = r.n(v), d = !0, m = d ? '/api/' : 'http://localhost:5000/api/', b = h.a.create({baseURL: m, timeout: 5e3, headers: {'Content-Type': 'application/json'}}); b.interceptors.request.use(function (e) { return e.headers['Authorization'] = 'Fake Token', e }), b.interceptors.response.use(function (e) { return e }, function (e) { return console.log(e), Promise.reject(e) }); var _ = {fetchResource: function () { return b.get('resource/xxx').then(function (e) { return e.data }) }, fetchSecureResource: function () { return b.get('secure-resource/zzz').then(function (e) { return e.data }) }}, g = {name: 'about', data: function () { return {resources: [], error: ''} }, methods: {fetchResource: function () { var e = this; _.fetchResource().then(function (t) { e.resources.push(t) }).catch(function (t) { e.error = t.message }) }}}, y = g, w = Object(a['a'])(y, l, p, !1, null, null, null), j = w.exports; n['a'].use(f['a']); var x = new f['a']({routes: [{path: '/', name: 'main', component: j}]}), O = r('L2JU'); n['a'].use(O['a']); var k = new O['a'].Store({state: {}, mutations: {}, actions: {}}), S = {formatTimestamp: function (e) { var t = new Date(e); return t.toLocaleTimeString('en-US') }}; Object.keys(S).forEach(function (e) { n['a'].filter(e, S[e]) }), n['a'].config.productionTip = !1, new n['a']({router: x, store: k, render: function (e) { return e(s) }}).$mount('#app') }, nNx0: function (e, t, r) { 'use strict'; var n = r('uWEC'), o = r.n(n); o.a }, uWEC: function (e, t, r) {}})
// # sourceMappingURL=app.6bf00515.js.map

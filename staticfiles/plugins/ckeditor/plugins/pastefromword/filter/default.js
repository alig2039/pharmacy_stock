/*
 Copyright (c) 2003-2018, CKSource - Frederico Knabben. All rights reserved.
 For licensing, see LICENSE.md or https://ckeditor.com/legal/ckeditor-oss-license
*/
(function(){function u(){return!1}function y(a,b){var c,d=[];a.filterChildren(b);for(c=a.children.length-1;0<=c;c--)d.unshift(a.children[c]),a.children[c].remove();c=a.attributes;var e=a,h=!0,f;for(f in c)if(h)h=!1;else{var l=new CKEDITOR.htmlPard


odoo.define('sh_project_task_issue_management.portal', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');
    var PortalSidebar = require('portal.PortalSidebar');
    var rpc = require('web.rpc');
    var core = require('web.core');
    var qweb = core.qweb;
    var _t = core._t;
    var Dialog = require("web.Dialog");
    var wysiwygLoader = require('web_editor.loader');


    publicWidget.registry.sh_issue = publicWidget.Widget.extend({
        selector: '.js_cls_issue_model',
        xmlDependencies: ["/sh_project_task_issue_management/static/src/xml/sh_issue_wizard_template.xml"],

        events: {
        },
        /**
             * @override
             */
        start: function () {




            var self = this;

            $('#sh_open_create_issue').click(function (ev) {
                var task_id = $(ev.target).attr('data-task-id')
                var project_id = $(ev.target).attr('data-project-id')
                var partner_id = $(ev.target).attr('data-partner-id')
                var user_id = $(ev.target).attr('data-user-id')
                var company_id = $(ev.target).attr('data-company-id')

                self._actionViewClick(task_id, project_id, partner_id, user_id, company_id)
            })
            this._super.apply(this, arguments);

        },
        _actionViewClick: async function (task_id, project_id, partner_id, user_id, company_id) {
            var self = this;
            var data = []
            await rpc.query({
                model: "sh.issue.type",
                method: "search_read",
                args: [],
            }).then(function (arrays) {
                data = arrays

            })

            var dialog = new Dialog(this, {
                title: _t("Create Issue"),
                $content: qweb.render("sh_create_issue", {
                    element: self,
                    'data': data
                }),

                buttons: [
                    {
                        text: _t("Create Issue"), classes: 'btn-primary', close: false,
                        click: (ev) => {
                            var name = $('#issueName').val()
                            ev.stopPropagation();
                            ev.preventDefault();
                            var issue_type = $('#selectIssueType').val()
                            var description = $('#selectDescription').val()
                            var environment = $('#selectEnvironment').val()
                            if (!name) {
                                alert("Please Enter Name")
                                $('#issueName').focus()
                                return false
                            } else if (!issue_type) {
                                alert("Please Select issue Type")
                                $('#selectIssueType').focus()
                            }
                            else {
                                var vals = {
                                    'name': name,
                                    'sh_issue_type_id': issue_type,
                                    'sh_partner_id': partner_id,
                                    'sh_company_id': company_id,
                                    'sh_task_id': task_id,
                                    'sh_project_id': project_id,
                                    'sh_user_ids': [user_id],
                                    'sh_description': description,
                                    'sh_additional_comment': environment,
                                }
                                this._rpc({
                                    model: 'sh.issue',
                                    method: 'portal_create',
                                    args: [vals],
                                }).then((callbak) => {
                                    location.reload();
                                })
                            }
                        }
                    },
                    {
                        text: _t("Cancel"), close: true
                    },
                ],
            });


            dialog.open().opened(async function () {

                var description_summernote = $(document).find('#selectDescription')
                description_summernote.summernote({
                    placeholder: 'Add Description Here',
                    height: 150,
                });
                var additional_comment_summernote = $(document).find('#selectEnvironment')
                additional_comment_summernote.summernote({
                    placeholder: 'Add Additional Note Here',
                    height: 150,
                });
            });
        },
    });
});

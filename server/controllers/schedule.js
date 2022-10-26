const scheduleRouter = require('express').Router()
const { parse, Parser } = require('json2csv')
const Task = require('../models/task')

scheduleRouter.get('/', async (req, res) => {
    const data = await Task.find({})
    const fields = ['worktime_duration', 'date', 'project_name', 'task_name', 'on_call',
        'overtime', 'invoice_note', 'first_name', 'last_name', 'supervisor', 'contract_type']
    const j2csvParser = new Parser({ fields })
    const csvData = j2csvParser.parse(data)
    res
        .setHeader('Content-disposition', 'attachment; filename=timesheet_report.csv')
        .set('Content-Type', 'text/csv')
        .send(csvData)
})

module.exports = scheduleRouter
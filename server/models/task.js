const mongoose = require('mongoose')

const taskSchema = new mongoose.Schema({
    contract_type: String,
    country: String,
    date: String,
    eficode_id: String,
    end_time: String,
    first_name: String,
    invoice_note: String,
    last_name: String,
    on_call: Boolean,
    overtime: Boolean,
    phase_name: String,
    project_customer: String,
    project_name: String,
    salary_category: String,
    salary_code: String,
    supervisor: String,
    task_name: String,
    worktime_duration: Number
})
taskSchema.set('toJSON', {
    transform: (document, returnedObject) => {
        returnedObject.id = returnedObject._id.toString()
        delete returnedObject._id
        delete returnedObject.id
        delete returnedObject.__v
        delete returnedObject.country
        delete returnedObject.end_time
        delete returnedObject.eficode_id
        delete returnedObject.project_customer
        delete returnedObject.salary_category
        delete returnedObject.salary_code
    }
})
module.exports = mongoose.model('demo', taskSchema, 'timesheet_demo')
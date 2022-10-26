const config = require('./utils/config')
const logger = require('./utils/logger')
const express = require('express')
const app = express()
const mongoose = require('mongoose')
const scheduleRouter = require('./controllers/schedule')

require('express-async-errors')

logger.info('connecting to ', config.PORT)
mongoose.connect(config.MONGODB_URI)
    .then(() => {
        logger.info('connected to MongoDB')
    }).catch((err) => {
        logger.error('error connecting to MongoDv', err.message)
    })

app.use(express.static('build'))
app.use(express.json())

app.use('/api/schedule', scheduleRouter)

module.exports = app
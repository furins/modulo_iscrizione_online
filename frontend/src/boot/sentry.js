import Vue from "vue";
import * as Sentry from "@sentry/vue";
import { Integrations } from "@sentry/tracing";

Sentry.init({
    Vue,
    dsn: process.env.SENTRY_DSN_URL,
    integrations: [new Integrations.BrowserTracing()],

    // We recommend adjusting this value in production, or using tracesSampler
    // for finer control
    tracesSampleRate: 1.0,
    release: '1.0.46'
});
Vue.prototype.$sentry = Sentry

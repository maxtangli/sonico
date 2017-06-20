# symfony source reading

language
- [x] VarDumper 1.3h // dirty magic addressing php defect: var_dump() not so obvious.
- [x] Debug 0.5h // dirty magic addressing php defect: no united exception, tedious debug options.
- [x] PropertyAccess 0.5h // dirty magic addressing php defect: no united access grammar.
- [x] PropertyInfo 1h // addressing php defect: reflection not so friendly.
- ClassLoader // deprecated in Symfony 3.3 and it will be removed in 4.0, use composer instead.
- [x] Serializer 0.8h // support json,xml,yaml,csv
- [ ] Filesystem
- [ ] Finder

cli
- [ ] Console
- [ ] OptionsResolver

http
- [ ] BrowserKit
- [ ] DomCrawler
- [ ] HttpFoundation
- [ ] HttpKernel
- [ ] Routing
- Ldap

view
- [ ] Validator
- [ ] Form
- [ ] CssSelector
- [x] Asset 0.5h // dedicated abstractions, browser game use case.
- [ ] Templating
- [ ] ExpressionLanguage
- [ ] Intl
- [ ] Translation

config
- [ ] Config
- [ ] Yaml
- [ ] Dotenv

components
- [ ] Process
- [ ] Cache
- [ ] DependencyInjection
- [ ] EventDispatcher
- [ ] Security
- [ ] Stopwatch
- [ ] Workflow
- PHPUnit Bridge
# AlmaViva MVP Product Blueprint

## Visão Geral
AlmaViva é uma plataforma SaaS que permite a empresas criarem linhas do tempo profissionais de sua história em aproximadamente 30 minutos. O produto combina upload de acervos (fotos, PDFs), coleta guiada de marcos históricos e um motor de IA que organiza o conteúdo cronologicamente para gerar dois entregáveis principais:

1. **Widget embutível**: código HTML responsivo que pode ser inserido em qualquer website corporativo.
2. **E-book profissional**: PDF pronto para impressão e compartilhamento.

## Público-Alvo
- Pequenas e médias empresas que buscam profissionalizar a apresentação de sua trajetória.
- Departamentos de marketing/comunicação de empresas de médio e grande porte.
- Consultorias de branding e agências digitais.

## Proposta de Valor
- Construa uma linha do tempo rica e visual em minutos, em vez de semanas.
- Disponibilize a história da empresa em múltiplos formatos sem precisar de equipe de design.
- Padronize e acelere iniciativas de employer branding, vendas e relações públicas.

## Métricas de Sucesso
- Tempo médio de conclusão do fluxo: ≤ 30 minutos.
- Taxa de conversão trial → pagamento: ≥ 20%.
- NPS ≥ 45 no trimestre pós-lançamento.
- Retenção mensal ≥ 85%.

## Personas Principais
1. **Marina, gerente de marketing**: precisa de um recurso rápido para atualizar o site corporativo com marcos recentes.
2. **Eduardo, fundador de startup**: quer uma narrativa visual para investidores em pouco tempo.
3. **Bianca, consultora de branding**: busca uma ferramenta escalável para entregar timelines a múltiplos clientes.

## Jornada do Usuário (MVP)
1. Cadastro e onboarding com trial de 7 dias.
2. Seleção ou criação de um projeto de linha do tempo.
3. Upload de documentos (fotos, PDFs, links) com extração automática de metadados.
4. Preenchimento de formulário guiado sobre marcos (data, título, descrição, categorias).
5. Revisão assistida por IA (sugestões de coerência, linguagem e datas).
6. Geração automática dos outputs (widget HTML + e-book PDF).
7. Personalização básica (cores corporativas, tipografia, imagem de capa).
8. Publicação e compartilhamento com analytics básicos (visualizações, downloads).

## Funcionalidades Essenciais (MVP - 3 meses)
- Autenticação e gerenciamento de contas multiusuário.
- Fluxo de upload com suporte a fotos (JPG/PNG) e documentos (PDF).
- Extração de texto e metadados usando serviços de OCR e análise documental.
- Formulário dinâmico para marcos, com validação e ordenação cronológica.
- Painel de edição da timeline com pré-visualização em tempo real.
- Motor de IA (OpenAI) para:
  - Resumir descrições longas.
  - Sugerir títulos e correções de data.
  - Gerar narrativa coesa para o e-book.
- Geração do widget responsivo (React embutido ou Web Components) com opção de incorporação via `<iframe>` ou script.
- Pipeline para renderização de e-book PDF (por exemplo, React-pdf ou Puppeteer).
- Integração com Stripe para planos recorrentes (€49,90, €99,90, €200/mês) com diferenciação por features (limite de timelines, usuários adicionais, branding avançado).
- Dashboard de analytics básicos.

## Roadmap Macro
- **Mês 1**
  - Finalizar escopo, UX flows e protótipos mobile-first.
  - Configurar infraestrutura (monorepo, CI/CD, ambientes dev/staging/prod).
  - Implementar autenticação, gestão de contas e Stripe checkout.

- **Mês 2**
  - Desenvolver fluxo completo de timeline: uploads, formulário de marcos, preview e ordenação cronológica.
  - Conectar serviço de IA da OpenAI para resumo/sugestões.
  - Iniciar geração de widget HTML e e-book PDF.

- **Mês 3**
  - Polir experiência mobile, testes de usabilidade, ajustes de performance.
  - Implementar analytics básicos e relatórios.
  - Preparar materiais de lançamento (landing page, tutoriais) e beta fechado.

## Arquitetura Técnica
- **Frontend (React + TypeScript)**
  - Framework sugerido: Next.js para SSR e performance.
  - UI library: Tailwind CSS ajustado às cores #1B365D e #F4D03F.
  - Estado global: Zustand ou Redux Toolkit conforme complexidade.
  - Uploads com drag-and-drop (react-dropzone) e preview em tempo real.

- **Backend (Node.js + Express ou NestJS)**
  - API REST/GraphQL para gerenciamento de projetos, marcos e assets.
  - Serviços para processamento assíncrono (fila com BullMQ/Redis) para OCR, IA e geração de PDFs.
  - Integração com OpenAI (gpt-4.1) para insights e narrativa.
  - Stripe Billing para planos e gestão de assinaturas.

- **Banco de Dados (PostgreSQL)**
  - Tabelas principais: `users`, `organizations`, `projects`, `milestones`, `assets`, `subscriptions`, `timeline_settings`.
  - Uso de Prisma ORM ou TypeORM.

- **Armazenamento de Arquivos**
  - Bucket S3 compatível (AWS S3 ou DigitalOcean Spaces) com CDN.
  - Processamento de imagens via Lambda/Cloud Functions para otimização.

- **Infraestrutura**
  - Deploy em plataforma gerenciada (Vercel para frontend, Render/Fly.io/Heroku para backend).
  - Monitoramento: Logtail + Sentry + Grafana/Prometheus (versão básica no MVP).
  - CI/CD: GitHub Actions com pipelines para testes, lint e deploy.

## Experiência do Usuário
- Design minimalista com predominância do azul marinho (#1B365D) e acentos dourados (#F4D03F).
- Layout mobile-first: cards responsivos, navegação em etapas, indicadores de progresso.
- Onboarding assistido com checklist de 30 minutos.
- Templates de timeline (linha contínua, mosaico, cards) com foco em tipografia limpa.

## Diferenciação dos Planos
| Plano | Preço (€/mês) | Limites principais | Recursos premium |
|-------|---------------|--------------------|------------------|
| Essencial | 49,90 | 3 projetos ativos, 3 usuários, 2GB uploads | Branding básico, exportação PDF padrão |
| Profissional | 99,90 | 10 projetos, 10 usuários, 10GB uploads | Branding avançado, colaboração em tempo real, remoção da marca AlmaViva |
| Enterprise | 200 | Projetos ilimitados, 30 usuários, 50GB uploads | SLA dedicado, integrações personalizadas, analytics avançado |

## Considerações de Compliance & Segurança
- Autenticação multifator opcional nos planos superiores.
- Armazenamento criptografado e HTTPS em toda a jornada.
- Conformidade com GDPR (ex.: consentimento para armazenar dados históricos de colaboradores).
- Auditoria de acesso a arquivos sensíveis.

## Roadmap Futuro (Pós-MVP)
- Editor avançado de design para o e-book (layouts customizados).
- Integração com LinkedIn/Facebook para distribuição da timeline.
- Templates setoriais com storytelling específico.
- Suporte multilíngue (pt/en/es) no front e outputs.
- Análise semântica para sugerir marcos ausentes com base nos documentos enviados.

## KPIs Técnicos
- TTFB < 1s na landing page.
- Geração de e-book < 2 minutos para projetos de até 100 marcos.
- Disponibilidade do serviço ≥ 99,5%.

## Riscos e Mitigações
- **Dependência da IA**: fallback com regras heurísticas se API estiver indisponível.
- **Privacidade de dados**: contrato e DPA claros, opções de exclusão de dados.
- **Qualidade dos uploads**: guias de boas práticas e filtros para arquivos corrompidos.

## Time & Recursos
- 1 Product Manager, 1 UX/UI, 2 Fullstack, 1 QA/DevOps.
- Reuniões semanais de alinhamento, sprints quinzenais.

## Go-to-Market Inicial
- Beta fechado com agências parceiras.
- Landing page com demonstrações interativas e depoimentos.
- Conteúdo educacional (webinars, artigos sobre storytelling corporativo).
- Parcerias com associações empresariais.

## Indicadores de Engajamento
- Taxa de conclusão do onboarding.
- Número de marcos por projeto.
- Frequência de exportação de e-book.
- Uso do widget (views, tempo médio na timeline).

## Suporte e Sucesso do Cliente
- Central de ajuda com tutoriais em vídeo.
- Chat suporte horário comercial (Zendesk ou Intercom).
- Reuniões trimestrais com clientes Enterprise.

## Requisitos de Marca
- Usar logotipo fornecido em todas as comunicações.
- Aplicar paleta azul marinho (#1B365D) e dourado (#F4D03F) com contraste adequado.
- Tipografia recomendada: Montserrat + Open Sans.

## Próximos Passos
1. Validar blueprint com stakeholders.
2. Criar protótipo navegável (Figma) das principais telas mobile/desktop.
3. Iniciar implementação conforme roadmap de 3 meses.


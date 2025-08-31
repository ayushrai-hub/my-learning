# 📚 Tech-Arsenal Resources

This directory contains learning resources that support the Tech-Arsenal curriculum. **Local PDFs** are stored in the `books/` directory, while other resources (papers, videos, tools, datasets) are referenced by **URL only** and cited directly in curriculum sections.

## 📁 Resource Organization

```
resources/
├── README.md              # This file - resource overview
├── topic-mapper.json      # Standardized topic-resource mapping database
├── resource-linking-template.md # Template for citing resources in curriculum
└── books/                 # PDF books and ebooks (LOCAL FILES ONLY)
```

**URL-Based Resources** (cited in curriculum sections):
- **Papers**: Research papers, whitepapers, and articles (URLs only)
- **Videos**: Video tutorials, courses, and recorded talks (URLs only)  
- **Tools**: Software tools, utilities, and online platforms (URLs only)
- **Datasets**: Sample datasets and data repositories (URLs only)

## 🔗 Topic Mapper System

The `topic-mapper.json` file provides a standardized way to link curriculum topics to resources:

- **Curriculum Topics**: Maps to specific sections in the curriculum
- **Resource Types**: Books, papers, videos, tools, datasets
- **Difficulty Levels**: Beginner, Intermediate, Advanced
- **Tags**: Searchable keywords for easy discovery
- **Quality Ratings**: Community-driven resource quality indicators

## 📖 Adding Resources

### 1. For PDF Books (Local Files)
```bash
# Add PDF to books directory
cp "Clean Architecture.pdf" resources/books/
```

### 2. Update Topic Mapper
Add resource metadata to `topic-mapper.json`:

**For Local PDF Books:**
```json
{
  "resource_id": "clean-architecture-martin",
  "title": "Clean Architecture: A Craftsman's Guide to Software Structure",
  "author": "Robert C. Martin",
  "type": "book",
  "file_path": "books/Clean Architecture.pdf",
  "url": null,
  "curriculum_topics": ["software-design", "backend-engineering"],
  "difficulty": "intermediate",
  "tags": ["architecture", "design-patterns", "clean-code"],
  "description": "Comprehensive guide to software architecture principles",
  "quality_rating": 5
}
```

**For URL-Based Resources:**
```json
{
  "resource_id": "fastapi-docs",
  "title": "FastAPI Documentation",
  "author": "Sebastian Ramirez",
  "type": "documentation",
  "file_path": null,
  "url": "https://fastapi.tiangolo.com/",
  "curriculum_topics": ["backend-engineering"],
  "difficulty": "beginner",
  "tags": ["fastapi", "api", "documentation"],
  "description": "Official FastAPI framework documentation",
  "quality_rating": 5
}
```

### 3. Cite in Curriculum
Add resource citations directly to relevant curriculum sections using the standardized template.

## 🎯 Resource Categories

### 📚 Books (`books/` - Local PDFs Only)
- Technical books (PDF format)
- Programming language guides
- System design and architecture books
- ML/AI engineering textbooks

### 📄 Papers (URL-Based, Cited in Curriculum)
- Research papers (arXiv, IEEE, ACM)
- Industry whitepapers
- Technical specifications
- Case studies and blog posts

### 🎥 Videos (URL-Based, Cited in Curriculum)
- YouTube tutorials and series
- Conference talks (YouTube, Vimeo)
- Online course platforms (Coursera, Udemy, etc.)
- Recorded workshops and webinars

### 🛠️ Tools (URL-Based, Cited in Curriculum)
- Online development tools and platforms
- Software documentation sites
- Interactive tutorials and playgrounds
- Development environment guides

### 📊 Datasets (URL-Based, Cited in Curriculum)
- Public dataset repositories (Kaggle, UCI, etc.)
- GitHub sample data repositories
- API documentation with examples
- Practice dataset collections

## 🔍 Finding Resources

### By Curriculum Topic
Use the topic mapper to find resources for specific curriculum sections:
```bash
# Find all resources for "ml-ai-engineering"
grep -r "ml-ai-engineering" topic-mapper.json
```

### By Resource Type
Browse specific resource types:
```bash
ls resources/books/          # All books
ls resources/papers/         # All papers
```

### By Difficulty Level
Filter resources by learning level using the topic mapper.

## 🤝 Contributing Resources

1. **Add the resource file** to the appropriate subdirectory
2. **Update topic-mapper.json** with resource metadata
3. **Test the links** to ensure curriculum integration works
4. **Submit a pull request** with your additions

See [`../docs/maintenance.md`](../docs/maintenance.md) for detailed contribution guidelines.

## 📋 Quality Standards

Resources should be:
- **High Quality**: Well-regarded in the community
- **Relevant**: Directly applicable to curriculum topics
- **Accessible**: Clear explanations and good structure
- **Current**: Up-to-date with modern practices
- **Legal**: Properly licensed or open source

## 🔧 Maintenance

- **Regular Updates**: Keep resources current with industry changes
- **Quality Review**: Community feedback on resource effectiveness
- **Link Validation**: Ensure curriculum-resource links work correctly
- **Organization**: Maintain clean directory structure and naming

---

**Next Steps**: 
1. Add your first resources to the appropriate directories
2. Update `topic-mapper.json` with resource metadata
3. Link resources in curriculum sections using the standardized format
